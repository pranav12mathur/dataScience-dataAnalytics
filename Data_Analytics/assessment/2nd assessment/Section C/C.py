'''
Mini Project: Food Delivery Order Management Console
Objective:
Build a console-based food delivery order management system that combines OOP, file
handling, functions, and exception handling into a single working application. The system must
allow a user to place orders, view all past orders, and search for a specific order — with all data
saved to and reloaded from a JSON file.
Your project must:
The program must be menu-driven with at least four options: (1) Place New Order, (2) View All
Orders, (3) Search Order by ID, (4) Exit.
Define a class Order with attributes: order_id (auto-generated), customer_name, items (list),
total_amount, and status ('Pending' by default).
On startup, load all existing orders from orders.json; save the updated orders list back to the
file after every new order is placed.
Validate all user inputs — catch non-numeric amounts, empty name fields, and missing file
errors — and display a clear message without crashing.
Display all orders in a formatted table showing order ID, customer name, item count, total
amount, and status; highlight orders with status 'Delivered' differently in the output.
'''
import json
import os
FILE_NAME = "orders.json"
class Order:
    next_id = 1

    def __init__(self, customer_name, items, total_amount, status="Pending"):
        self.order_id = Order.next_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = status
        Order.next_id += 1

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amount": self.total_amount,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        order = cls(
            customer_name=data.get("customer_name", "Unknown"),
            items=data.get("items", []),
            total_amount=float(data.get("total_amount", 0.0)),
            status=data.get("status", "Pending"),
        )
        order.order_id = int(data.get("order_id", order.order_id))
        return order


def load_orders():
    try:
        if not os.path.exists(FILE_NAME):
            save_orders([])
            return []

        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Warning: orders.json does not contain a valid list. Starting fresh.")
            save_orders([])
            return []

        orders = []
        max_id = 0
        for entry in data:
            try:
                order = Order.from_dict(entry)
                orders.append(order)
                max_id = max(max_id, order.order_id)
            except Exception:
                continue

        Order.next_id = max_id + 1
        return orders

    except FileNotFoundError:
        print("File not found. Creating a new orders.json file.")
        save_orders([])
        return []
    except json.JSONDecodeError:
        print("The order file is empty or invalid. Starting with a new list.")
        save_orders([])
        return []
    except Exception as e:
        print("Unexpected error while loading orders:", e)
        save_orders([])
        return []


def save_orders(orders):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump([order.to_dict() for order in orders], file, indent=4)
    except FileNotFoundError:
        print("Error: The file path is missing. Can't save orders.")
    except Exception as e:
        print("Error while saving orders:", e)


def get_valid_name(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Customer name cannot be empty.")


def place_new_order(orders):
    print("\n--- Place New Order ---")
    customer_name = get_valid_name("Enter customer name: ")

    items = []
    total_amount = 0.0

    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").strip()
        if item_name.lower() == "done":
            if not items:
                print("Error: Please add at least one item before finishing the order.")
                continue
            break

        if not item_name:
            print("Error: Item name cannot be empty.")
            continue

        try:
            item_price = float(input(f"Enter price for '{item_name}': ").strip())
            if item_price <= 0:
                raise ValueError
        except ValueError:
            print("Error: Please enter a valid positive numeric price.")
            continue

        items.append(item_name)
        total_amount += item_price

    order = Order(customer_name, items, total_amount)
    orders.append(order)
    save_orders(orders)
    print("Order placed successfully! Order ID:", order.order_id)
    print("Customer:", order.customer_name)
    print("Items:", ", ".join(order.items))
    print("Total Amount:", "$" + str(format(order.total_amount, '.2f')))


def display_orders(orders):
    print("\n--- All Orders ---")
    if not orders:
        print("No orders found.")
        return

    print("Order ID   Customer             Items        Amount      Status")
    print("---------------------------------------------------------------")

    for order in orders:
        item_count = len(order.items)
        amount = "$" + str(format(order.total_amount, '.2f'))
        status = order.status

        if status == "Delivered":
            print(order.order_id, order.customer_name, item_count, amount, "[DELIVERED]")
        else:
            print(order.order_id, order.customer_name, item_count, amount, status)


def search_order(orders):
    print("\n--- Search Order by ID ---")
    try:
        order_id = int(input("Enter order ID: ").strip())
    except ValueError:
        print("Error: Order ID must be a number.")
        return

    found = False
    for order in orders:
        if order.order_id == order_id:
            found = True
            print("Order found:")
            print("Order ID:", order.order_id)
            print("Customer:", order.customer_name)
            print("Items:", ", ".join(order.items) if order.items else "No items")
            print("Total Amount:", "$" + str(format(order.total_amount, '.2f')))
            print("Status:", order.status)
            if order.status == "Delivered":
                print("Status Highlight: [DELIVERED]")
            break

    if not found:
        print("No order found with ID", order_id, ".")


def main():
    print("Welcome to the Food Delivery Order Management Console!")
    orders = load_orders()

    while True:
        print("\nMenu")
        print("1. Place New Order")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): ").strip())
        except ValueError:
            print("Error: Please enter a valid number from 1 to 4.")
            continue

        if choice == 1:
            place_new_order(orders)
        elif choice == 2:
            display_orders(orders)
        elif choice == 3:
            search_order(orders)
        elif choice == 4:
            print("Thank you for using the Food Delivery Order Management Console. Goodbye!")
            break
        else:
            print("Error: Invalid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
