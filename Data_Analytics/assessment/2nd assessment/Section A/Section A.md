#  Section A — Concept Application

## 1. SCENARIO
You are building a food delivery app that tracks four values per order: the order total (Rs
499D.50), the delivery distance (7.3 km), the payment method ('UPI'), and whether the
restaurant is currently accepting orders (True).

**Question:** Identify the correct Python data type for each of the four values above. Then explain
why assigning the wrong type — for example, storing Rs 499.50 as an integer — would cause an
incorrect result when applying a 10% discount calculation.

**answers**
```
data type for order total : float
data type for delivery distance : float
data type for payment method : str
data type for restaurant status : bool
assigning the wrong type for order total, such as storing it as an integer, would lead to incorrect calculations when applying a 10% discount. For example, if the order total is stored as an integer (499), applying a 10% discount would result in 49.9, which would be truncated to 49 when stored as an integer, leading to an incorrect final price of 450 instead of the correct 449.55. Using the correct float type ensures that decimal values are preserved and calculations are accurate.
```


## 2. SCENARIO
You are developing a restaurant menu system. A teammate suggests storing the menu
as a list of tuples like [('Paneer Burger', 180, 'Snacks'), ('Masala Dosa', 90, 'Breakfast')],
while you prefer a dictionary where each dish name is the key.

**Question:** Compare these two data structures for looking up a dish price by name. Which gives
faster and more readable access, and why? Describe one limitation of the list-of-tuples
approach that the dictionary design solves.

**answers**
```
- tuple is an immutable data structure that can hold multiple values, while a dictionary is a mutable data structure that stores key-value pairs.
- For looking up a dish price by name, a dictionary provides faster and more readable access because it allows direct access to the value associated with a specific key (dish name) using the syntax menu[dish_name], which is O(1) time complexity. In contrast, looking up a dish price in a list of tuples requires iterating through the list and checking each tuple for a match, resulting in O(n) time complexity.
- One limitation of the list-of-tuples approach is that it does not provide a straightforward way to update or remove a dish from the menu. In a dictionary, you can easily update the price of a dish or remove it by using the key, while in a list of tuples, you would need to find the tuple, create a new tuple with the updated value, and replace it in the list, which is less efficient and more error-prone.                       
```

## 3. SCENARIO
You are writing a delivery fee calculator that applies three different fee rules: no charge
if the order value is Rs 500 or more, Rs 30 fee if distance is 5 km or less, and Rs 60 fee for
distances above 5 km. A colleague proposes writing this as a single lambda function.

**Question:** Explain why a named function defined with def is more appropriate than a lambda
for this multi-condition fee logic. Then describe one specific situation inside this same app where
a lambda would genuinely be the better choice.

**answers**
```
A named function defined with def is more appropriate than a lambda for this multi-condition fee logic because it allows for better readability and maintainability of the code. A named function can have a descriptive name that indicates its purpose, making it easier for other developers (or even the original developer at a later time) to understand what the function does. Additionally, a named function can include multiple lines of code, comments, and complex logic, which is not possible with a lambda function that is limited to a single expression.
```

## 4. SCENARIO
You are working on an order history feature that must save completed delivery orders to
a JSON file so the system can reload all orders when the app restarts.

**Question:** Describe the complete Python sequence to write a single order dictionary to a JSON
file and read it back. What exception is raised if the file does not exist at read time, and how
should your program handle it so the app starts cleanly on its first run?

**answers**
```python
import json

# Writing to JSON file
order = {"id": 1, "total": 499.50, "distance": 7.3, "payment_method": "UPI", "restaurant_accepting": True}
with open("orders.json", "w") as f:
    json.dump(order, f)

# Reading from JSON file
with open("orders.json", "r") as f:
    order = json.load(f)
'''
exception is raised if the file does not exist at read time: FileNotFoundError. To handle this, you can use a try-except block to catch the exception and initialize an empty list or dictionary for orders if the file does not exist, allowing the app to start cleanly on its first run.
'''
```
## 5. SCENARIO
You are designing a delivery tracking system. Each delivery must store the rider's name,
current GPS location, assigned order ID, and status (e.g. 'On the way'). It must also
support actions such as updating the location and marking the delivery as complete.

**Question:** Justify why a class is a better design choice here than storing all of this data in
separate variables or a plain dictionary. Identify at least two OOP principles your class design
would apply and explain what each one achieves.

**answers**
```
Class is a better design choice for the delivery tracking system because it allows for encapsulation of related data and behaviors into a single entity. This makes the code more organized, reusable, and easier to maintain. By using a class, you can define methods that operate on the delivery data, such as updating the location or marking the delivery as complete, which would be cumbersome to manage with separate variables or a plain dictionary.
Two OOP principles that the class design would apply are:
1. Encapsulation: This principle allows the class to bundle the delivery data (rider's name, GPS location, order ID, status) and the methods that operate on that data (update location, mark as complete) into a single unit. This helps protect the internal state of the object and provides a clear interface for interacting with it.
2. Abstraction: This principle allows the class to hide the complex implementation details of the delivery tracking system and expose only the necessary functionalities to the user. For example, users of the class can update the location or mark the delivery as complete without needing to know how these actions are implemented internally, making the system easier to use and understand.
```

## 6. SCENARIO
You are debugging a delivery cost calculator. When a user types 'two hundred' instead
of a number for the order amount, the program crashes with an unhandled exception.

**Question:** Describe how you would use a try-except block to handle this error gracefully. Name
the specific exception type you would catch, and explain how you would structure the code so
the program asks the user to re-enter the value instead of terminating.

```
To handle the error gracefully, I would use a try-except block to catch the ValueError exception that occurs when trying to convert a non-numeric string to a float or integer. The code would be structured in a loop that continues to prompt the user for input until a valid numeric value is entered. Here's an example of how this could be implemented:
```
```python
while True:
    user_input = input("Please enter the order amount: ")
    try:
        order_amount = float(user_input)  
        break  
    except ValueError:
        print("Invalid input. Please enter a numeric value for the order amount.")
```
