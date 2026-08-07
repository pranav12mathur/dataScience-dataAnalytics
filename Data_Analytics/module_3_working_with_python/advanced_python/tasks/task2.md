# Case-Based Tasks on Conditional Statements in Python

## Task 1: Student Grade Calculator
Write a Python program to input student marks and display the grade:
- 90 and above: Grade A
- 75 to 89: Grade B
- 50 to 74: Grade C
- 35 to 49: Grade D
- Below 35: Fail

```python
marks =int(input("Enter your marks:"))
if marks>=90:
    print("Your grade is A")
elif marks>=75:
    print("Your grade is B")
elif marks>=50:
    print("Your grade is C")
elif marks>=35:
    print("Your grade is D")
else:
    print("You have failed")
```

## Task 2: Electricity Bill Calculator
Write a Python program to calculate electricity charges based on units consumed:
- First 100 units: ₹5/unit
- Next 100 units: ₹7/unit
- Above 200 units: ₹10/unit

```python
units = int(input("Enter electricity units:"))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print("Your electricity bill is: ₹", bill)
```

## Task 3: Age Category Checker
Write a Python program to check a person's category based on age:
- Below 13: Child
- 13 to 19: Teenager
- 20 to 59: Adult
- 60 and above: Senior Citizen

```python
age = int(input("Enter your age:"))
if age<13:
    print("You are a child")
elif age<=19:
    print("You are a teenager")
elif age <=59:
    print("You are an adult")
else:
    print("You are a Senior citizen")
```

## Task 4: Number Checker
Write a Python program to check whether a number is:
- Positive
- Negative
- Zero

```python
number = int(input("Enter a number:"))
if number>0:
    print("Number is postive")
elif number<0:
    print("Number is negative")
else:
    print("Number is zero")
```

## Task 5: Even or Odd Number
Write a Python program to check whether the entered number is even or odd.

```python
n = int(input("Enter a number:"))
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")
```

## Task 6: Largest Among Three Numbers
Write a Python program to input three numbers and find the largest number using conditional statements.

```python
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))
if a>b and a>c:
    print("1st number is greater")
elif b>a and b>c:
    print("2nd number is greater")
else:
    print("3rd number is greater")
```

## Task 7: Driving License Eligibility
Write a Python program to check driving license eligibility:
- Age 18 or above: Eligible
- Below 18: Not Eligible

```python
age = int(input("Enter your age:"))
if age>=18:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")
```

## Task 8: Temperature Checker
Write a Python program to display weather conditions:
- Below 10°C: Cold
- 10°C to 30°C: Normal
- Above 30°C: Hot

```python
temp = int(input("Enter the temperature:"))
if temp<10:
    print("It is cold")
elif temp<=30:
    print("It is Normal")
else:
    print("It is hot")
```

## Task 9: Login Authentication System
Write a Python program to check username and password:
- Correct username and password: Login Successful
- Wrong details: Invalid Login

```python
us = "John"
pas = "John123"
u = input("Enter your username:")
p = input("Enter your password:")
if u==us and p==pas:
    print("Login successfull")
elif u==us and p!=pas:
    print("Invalid details")
elif u!=us and p==pas:
    print("Invalid details")
else:
    print("Invalid details")
```

## Task 10: Simple Calculator
Write a Python program to perform operations based on user choice:
- Addition
- Subtraction
- Multiplication
- Division

```python
print("***************Calculator***************")
print("Enter your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    choice = int(input("Enter your choice:"))
    if choice==1:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Addition is:",a+b)
    elif choice==2:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Subtraction is:",a-b)
    elif choice==3:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Multiplication is:",a*b)
    elif choice==4:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Division is:",a/b)
    else:
        print("Invalid choice")
    break
```

## Task 11: Employee Bonus Calculator
Write a Python program to calculate employee bonus:

- Salary above ₹50000: 20% bonus
- Salary between ₹30000 and ₹50000: 10% bonus
- Below ₹30000: 5% bonus

```python
salary = int(input("Enter your salary:"))
if salary>50000:
    bonus = salary * 0.2
elif salary>=30000:
    bonus = salary * 0.1
else:
    bonus = salary * 0.05
print("Your bonus is: ₹", bonus)
```

## Task 12: Movie Ticket Price Calculator
Write a Python program to calculate ticket price:
- Age below 12: ₹100
- Age 12 to 60: ₹200
- Age above 60: ₹150

```python
age = int(input("Enter your age:"))
if age<12:
    price = 100
elif age<=60:
    price = 200
else:
    price = 150
print("Your ticket price is: ₹", price)
```

## Task 13: Bank Withdrawal System
Write a Python program to check withdrawal:
- Balance sufficient: Allow withdrawal
- Insufficient balance: Show error message

```python
b = 10000
w = int(input("Enter the withdrawl amount:"))
if w<=b:
    print("Allow withdrawl")
else:
    print("Insufficient balance")
```

## Task 14: Shopping Discount Calculator
Write a Python program to apply discount:
- Purchase above ₹10000: 20% discount
- Purchase above ₹5000: 10% discount
- Otherwise: No discount

```python
p = int(input("Enter your purchase amount:"))
if p>10000:
    discount = p * 0.2
elif p>5000:
    discount = p * 0.1
else:
    discount = 0
print("Your discount is: ₹", discount)
```

## Task 15: Traffic Signal System
Write a Python program to display action based on traffic light color:
- Red: Stop
- Yellow: Wait
- Green: Go

```python
t = input("Enter traffic light colour:")
if t=="Red":
    print("Stop")
elif t=="Yellow":
    print("Wait")
else:
    print("Go")
```

## Task 16: Voter Eligibility Checker
Write a Python program to check voting eligibility:
- Age 18 or above: Eligible to vote
- Below 18: Not eligible to vote

```python
age = int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

## Task 17: Password Strength Checker
Write a Python program to check password strength:
- Length less than 6: Weak
- Length 6 to 10: Medium
- Length above 10: Strong

```python
p = input("Enter your password:")
if len(p)<6:
    print("Weak password")
elif len(p)<=10:
    print("Medium password")
else:
    print("Strong password")
```

## Task 18: BMI Category Calculator
Write a Python program to calculate BMI category:
- BMI below 18.5: Underweight
- 18.5 to 24.9: Normal
- 25 to 29.9: Overweight
- 30 and above: Obese

```python
b = float(input("Enter your BMI:"))
if b<18.5:
    print("Underweight")
elif b<=24.9:
    print("Normal")
elif b<=29.9:
    print("Overweight")
else:
    print("Obese")
```

## Task 19: Mobile Data Plan Selector
Write a Python program to suggest a mobile plan:
- Data usage below 2GB: Basic Plan
- 2GB to 5GB: Standard Plan
- Above 5GB: Premium Plan

```python
d = float(input("Enter your data usage in GB:"))
if d<2:
    print("Basic Plan")
elif d<=5:
    print("Standard Plan")
else:
    print("Premium Plan")
```

## Task 20: Exam Result Checker
Write a Python program to display result:
- All subjects marks >= 35: Pass
- Any subject below 35: Fail
- Marks above 90 in all subjects: Excellent Performance
```python
marks = int(input("Enter your all subject marks:"))
if marks>=35:
    print("You are Pass")
elif marks<35:
    print("You are fail")
else:
    print("Excellent Performance")
```