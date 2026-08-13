'''
Task 3: Order History File Logger
Build a program that records food delivery orders to a JSON file and lets the user view all past
orders, demonstrating file handling and exception handling together.
Accept the following order details from the user: customer name, list of items
(comma-separated input converted to a Python list), total amount, and order status.
Load the existing orders list from orders.json before adding the new order, then save the
updated list back to the file — so all orders accumulate across runs.
Provide a 'View Orders' option that reads orders.json and prints each order in a readable
format.
Use a try-except block to handle FileNotFoundError (first run, no file yet) and ValueError
(non-numeric total amount).
'''
import json
def load_orders():
    try:
        with open("orders.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_orders(orders):
    with open("orders.json", "w") as f:
        json.dump(orders, f)
def view_orders():
    orders = load_orders()
    for i, order in enumerate(orders, start=1):
        print(f"Order {i}:")
        print(f"  Customer: {order['customer_name']}")
        print(f"  Items: {', '.join(order['items'])}")
        print(f"  Total Amount: {order['total_amount']}")
        print(f"  Status: {order['status']}")
        print()
def add_order():
    customer_name = input("Enter customer name: ")
    items_input = input("Enter items (comma-separated): ")
    items = [item.strip() for item in items_input.split(",")]
    while True:
        try:
            total_amount = float(input("Enter total amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the total amount.")
    status = input("Enter order status: ")
    order = {
        "customer_name": customer_name,
        "items": items,
        "total_amount": total_amount,
        "status": status
    }
    orders = load_orders()
    orders.append(order)
    save_orders(orders)
while True:
    print("\nOrder History File Logger")
    print("1. Add Order")
    print("2. View Orders")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_order()
    elif choice == '2':
        view_orders()
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")