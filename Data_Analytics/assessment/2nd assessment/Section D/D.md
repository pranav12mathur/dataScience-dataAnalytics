# 1. Prompt given to the AI tool
```
Write a Python program that calculates a delivery order bill.
Requirements:
1. Accept a list of food items and their prices from the user to calculate the itemised subtotal.
2. Calculate an 18% GST charge and a flat Rs 30 delivery fee.
3. Ask for the number of previous orders. If previous orders > 5, apply a 10% loyalty discount on the subtotal.
4. Calculate and print a clear, formatted receipt showing line items (subtotal, GST, delivery fee, discount if applicable, and total payable).
5. Handle invalid inputs such as negative prices or non-numeric order counts using try-except blocks or validation loops.
```

# 2. Code comparison

**AI's original code**
```python
# AI-generated implementation
def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Price cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_non_negative_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Order count cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("--- Food Delivery Order Builder ---")
    items = []
    
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        if not item_name:
            print("Item name cannot be empty.")
            continue
            
        price = get_positive_float(f"Enter price for '{item_name}': Rs ")
        items.append((item_name, price))
    
    if not items:
        print("No items added. Exiting program.")
        return

    previous_orders = get_non_negative_int("Enter number of previous orders placed: ")

    subtotal = sum(price for _, price in items)
    
    # Calculate discount
    discount = 0.0
    if previous_orders > 5:
        discount = subtotal * 0.10
    
    subtotal_after_discount = subtotal - discount
    
    # AI Logic Bug: Tax is calculated on original subtotal, ignoring discount
    gst = subtotal * 0.18  
    delivery_fee = 30.0 if subtotal > 0 else 0.0
    
    final_total = subtotal - discount + gst + delivery_fee

    # Formatted Receipt
    print("\n" + "="*35)
    print("           RECEIPT           ")
    print("="*35)
    for name, price in items:
        print(f"{name:<20} Rs {price:>7.2f}")
    print("-" * 35)
    print(f"{'Subtotal':<20} Rs {subtotal:>7.2f}")
    if discount > 0:
        print(f"{'Loyalty Discount (10%)':<20} -Rs {discount:>7.2f}")
    print(f"{'GST (18%)':<20} Rs {gst:>7.2f}")
    print(f"{'Delivery Fee':<20} Rs {delivery_fee:>7.2f}")
    print("="*35)
    print(f"{'Total Amount Payable':<20} Rs {final_total:>7.2f}")
    print("="*35)

if __name__ == "__main__":
    main()
```

**Corrected Code**
```python
# Corrected implementation
def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Price must be greater than zero. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid numerical price.")

def get_non_negative_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Order count cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

def main():
    print("--- Food Delivery Order Builder ---")
    items = []
    
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        if not item_name:
            print("Item name cannot be empty.")
            continue
            
        price = get_positive_float(f"Enter price for '{item_name}': Rs ")
        items.append((item_name, price))
    
    if not items:
        print("No items added. Order canceled.")
        return

    previous_orders = get_non_negative_int("Enter number of previous orders placed: ")

    subtotal = sum(price for _, price in items)
    
    # Apply loyalty discount
    discount = (subtotal * 0.10) if previous_orders > 5 else 0.0
    taxable_subtotal = subtotal - discount
    
    # FIX: GST must be calculated on the post-discount taxable subtotal
    gst = taxable_subtotal * 0.18  
    delivery_fee = 30.00
    
    final_total = taxable_subtotal + gst + delivery_fee

    # Formatted Receipt
    print("\n" + "="*40)
    print(f"{'ITEMISED RECEIPT':^40}")
    print("="*40)
    for name, price in items:
        print(f"{name:<25} Rs {price:>8.2f}")
    print("-" * 40)
    print(f"{'Subtotal':<25} Rs {subtotal:>8.2f}")
    if discount > 0:
        print(f"{'Loyalty Discount (10%)':<25} -Rs {discount:>8.2f}")
    print(f"{'GST (18%)':<25} Rs {gst:>8.2f}")
    print(f"{'Delivery Fee':<25} Rs {delivery_fee:>8.2f}")
    print("="*40)
    print(f"{'Total Amount Payable':<25} Rs {final_total:>8.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
```

# 3. Bug Fix Explanation Note

```
The AI calculated GST on the gross subtotal (subtotal * 0.18) instead of the post-discount taxable amount (taxable_subtotal * 0.18), which overcharges customers when discounts apply. Additionally, the original validation allowed a 0.0 price, which is invalid for commercial menu items. I updated the tax computation to run on subtotal - discount and tightened price validation to enforce positive values (val > 0).
```