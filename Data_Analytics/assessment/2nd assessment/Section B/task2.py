'''
Build a menu management program that stores a restaurant's menu in a dictionary and lets
the user interact with it through a looped console interface.
- Store at least 6 menu items in a dictionary; each item maps a dish name (key) to a nested
dictionary with keys: price and category.
- Provide three options in a loop: (1) View all items formatted as a numbered table, (2) Filter
items by category, (3) Search for a dish by name and display its price.
- Define a separate function for each of the three operations; call them from the main loop.
- Keep the loop running until the user enters '0' to exit
'''
menu = {
    "Burger": {"price": 150, "category": "Main Course"},
    "Pizza": {"price": 250, "category": "Main Course"},
    "Salad": {"price": 100, "category": "Starters"},
    "Pasta": {"price": 200, "category": "Main Course"},
    "Ice Cream": {"price": 50, "category": "Desserts"},
    "Soda": {"price": 30, "category": "Beverages"}
}
def view_all_items(menu):
    print("\nMenu Items:")
    print("{:<5} {:<15} {:<10} {:<15}".format("No.", "Dish Name", "Price", "Category"))
    for i, (dish, details) in enumerate(menu.items(), start=1):
        print("{:<5} {:<15} {:<10} {:<15}".format(i, dish, details["price"], details["category"]))
def filter_items_by_category(menu, category):
    print(f"\nItems in category '{category}':")
    print("{:<5} {:<15} {:<10} {:<15}".format("No.", "Dish Name", "Price", "Category"))
    for i, (dish, details) in enumerate(menu.items(), start=1):
        if details["category"] == category:
            print("{:<5} {:<15} {:<10} {:<15}".format(i, dish, details["price"], details["category"]))
def search_dish_by_name(menu, dish_name):
    if dish_name in menu:
        details = menu[dish_name]
        print(f"\nDish: {dish_name}")
        print(f"Price: {details['price']}")
        print(f"Category: {details['category']}")
    else:
        print(f"\nDish '{dish_name}' not found.")
while True:
    print("\nMenu Management Program")
    print("1. View all items")
    print("2. Filter items by category")
    print("3. Search for a dish by name")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_all_items(menu)
    elif choice == '2':
        category = input("Enter category to filter by: ")
        filter_items_by_category(menu, category)
    elif choice == '3':
        dish_name = input("Enter dish name to search: ")
        search_dish_by_name(menu, dish_name)
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")