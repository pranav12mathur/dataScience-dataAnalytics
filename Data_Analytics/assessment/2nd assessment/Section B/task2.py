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
while True:
    print("")