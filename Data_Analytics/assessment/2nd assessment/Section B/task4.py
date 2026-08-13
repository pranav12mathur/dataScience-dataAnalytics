'''
Task 4: Delivery Rider OOP System
Build an object-oriented system that models delivery riders using a class, stores multiple rider
objects in a list, and persists their data to a CSV file.
Create a Rider class with instance attributes: rider_id, name, status (default 'Available'), and
total_deliveries (default 0).
Implement three methods: assign_order(order_id) — sets status to 'On Delivery' and prints a
confirmation; complete_delivery() — increments total_deliveries, resets status to 'Available';
display_info() — prints all rider details.
In the main program, create at least three Rider objects and provide a simple numbered menu
to assign and complete orders for any rider selected by ID.
Save all rider data to riders.csv using the csv module when the user exits, and reload it at
program start if the file exists.
'''
import csv
import os
class Rider:
    def __init__(self, rider_id, name, status="Available", total_deliveries=0):
        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = int(total_deliveries)
    def assign_order(self, order_id):
        self.status = "On Delivery"
        print(f"\nOrder {order_id} assigned to Rider {self.name}.")
    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print(f"\nDelivery completed for Rider {self.name}.")
    def display_info(self):
        print(f"ID: {self.rider_id} | Name: {self.name:<12} | Status: {self.status:<12} | Total: {self.total_deliveries}")



FILENAME = "riders.csv"

def load_riders():
    riders = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                riders.append(Rider(
                    row["rider_id"], 
                    row["name"], 
                    row["status"], 
                    row["total_deliveries"]
                ))
        print("Existing data loaded from CSV.")
    else:
        riders = [
            Rider("R1", "Alice"),
            Rider("R2", "Bob"),
            Rider("R3", "Charlie")
        ]
        print("No existing data found. Initialized default riders.")
    return riders
def save_riders(riders):
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["rider_id", "name", "status", "total_deliveries"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for r in riders:
            writer.writerow({
                "rider_id": r.rider_id,
                "name": r.name,
                "status": r.status,
                "total_deliveries": r.total_deliveries
            })
    print("Data saved to CSV successfully.")


def main():
    riders_list = load_riders()
    while True:
        print("\n" + "="*40)
        print("     DELIVERY RIDER MANAGEMENT SYSTEM")
        print("="*40)
        print("1. View All Riders")
        print("2. Assign Order to Rider")
        print("3. Complete Order for Rider")
        print("4. Save and Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            print("\n--- Current Riders Status ---")
            for r in riders_list:
                r.display_info()
        elif choice == "2":
            target_id = input("Enter Rider ID to assign: ").strip()
            rider = next((r for r in riders_list if r.rider_id == target_id), None)
            if rider:
                if rider.status == "On Delivery":
                    print("Error: This rider is already busy on an active delivery!")
                else:
                    order_id = input("Enter Order ID: ").strip()
                    rider.assign_order(order_id)
            else:
                print("Error: Rider ID not found.") 
        elif choice == "3":
            target_id = input("Enter Rider ID completing order: ").strip()
            rider = next((r for r in riders_list if r.rider_id == target_id), None)
            if rider:
                if rider.status == "Available":
                    print("Error: This rider does not have an active delivery to complete.")
                else:
                    rider.complete_delivery()
            else:
                print("Error: Rider ID not found.")
        elif choice == "4":
            print("\nExiting system...")
            save_riders(riders_list)
            break
        else:
            print("Error: Invalid selection. Please choose 1-4.")
if __name__ == "__main__":
    main()
