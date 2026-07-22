#  Section A — Concept Application

## 1. SCENARIO
You are building a food delivery app that tracks four values per order: the order total (Rs
499D.50), the delivery distance (7.3 km), the payment method ('UPI'), and whether the
restaurant is currently accepting orders (True).

**Question:** Identify the correct Python data type for each of the four values above. Then explain
why assigning the wrong type — for example, storing Rs 499.50 as an integer — would cause an
incorrect result when applying a 10% discount calculation.


## 2. SCENARIO
You are developing a restaurant menu system. A teammate suggests storing the menu
as a list of tuples like [('Paneer Burger', 180, 'Snacks'), ('Masala Dosa', 90, 'Breakfast')],
while you prefer a dictionary where each dish name is the key.

**Question:** Compare these two data structures for looking up a dish price by name. Which gives
faster and more readable access, and why? Describe one limitation of the list-of-tuples
approach that the dictionary design solves.


## 3. SCENARIO
You are writing a delivery fee calculator that applies three different fee rules: no charge
if the order value is Rs 500 or more, Rs 30 fee if distance is 5 km or less, and Rs 60 fee for
distances above 5 km. A colleague proposes writing this as a single lambda function.

**Question:** Explain why a named function defined with def is more appropriate than a lambda
for this multi-condition fee logic. Then describe one specific situation inside this same app where
a lambda would genuinely be the better choice.


## 4. SCENARIO
You are working on an order history feature that must save completed delivery orders to
a JSON file so the system can reload all orders when the app restarts.

**Question:** Describe the complete Python sequence to write a single order dictionary to a JSON
file and read it back. What exception is raised if the file does not exist at read time, and how
should your program handle it so the app starts cleanly on its first run?


## 5. SCENARIO
You are designing a delivery tracking system. Each delivery must store the rider's name,
current GPS location, assigned order ID, and status (e.g. 'On the way'). It must also
support actions such as updating the location and marking the delivery as complete.

**Question:** Justify why a class is a better design choice here than storing all of this data in
separate variables or a plain dictionary. Identify at least two OOP principles your class design
would apply and explain what each one achieves.


## 6. SCENARIO
You are debugging a delivery cost calculator. When a user types 'two hundred' instead
of a number for the order amount, the program crashes with an unhandled exception.

**Question:** Describe how you would use a try-except block to handle this error gracefully. Name
the specific exception type you would catch, and explain how you would structure the code so
the program asks the user to re-enter the value instead of terminating.

