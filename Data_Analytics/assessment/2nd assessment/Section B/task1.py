'''
Task 1: Delivery Fee Calculator
Build a console program that calculates and displays the final bill for a food delivery order
based on order value and delivery distance.
- Prompt the user to enter the order value (Rs ) and delivery distance (km) as separate inputs.
- Apply these fee rules using conditional statements: free delivery if order value >= Rs 500; Rs 30
fee if distance <= 5 km; Rs 60 fee if distance > 5 km.
- Display the item total, delivery fee, and final amount payable in a clearly formatted output.
- Handle the case where the user enters a negative distance or negative order value by printing
an appropriate error message and stopping execution.
'''
print("***************Delivery Fee Calculator***************")
order_value = float(input("Enter the order value (Rs): "))
delivery_distance = float(input("Enter the delivery distance (km): "))
if order_value < 0 or delivery_distance < 0:
    print("Error: Order value and delivery distance must be positive numbers.")
else:
    if order_value >= 500:
        delivery_fee = 0
    elif delivery_distance <= 5:
        delivery_fee = 30
    else:
        delivery_fee = 60
    item_total = order_value
    final_amount = item_total + delivery_fee
    print("\n***************Bill Details***************")
    print("Item total: Rs {:.2f}".format(item_total))
    print("Delivery Fee: Rs {:.2f}".format(delivery_fee))
    print("Final Amount Payable: Rs {:.2f}".format(final_amount))