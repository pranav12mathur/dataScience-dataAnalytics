#  H.W 
# w.a.p to print naturals numbers
print("Natural numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")
# w.a.p to print 1 to 10 numbers and find odd numbers only 
print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")
# w.a.p to print 1 to 10 numbers and find even numbers only
print("Even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")
# w.a.p to find infinite loop 
"""
print("Infinte loop:")
i = 0
while True:
    print("Hello World")
    i = i + 1
"""
# w.a.p to find factorials numbers 
print("Factorial of numbers from 1 to 5:")
for i in range(1, 6):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print("Factorial of", i, "is", factorial)
print("\n")
# w.a.p to find armstrong numbers 
print("Armstrong numbers from 1 to 10:")
for i in range(1,11):
    sum_of_cubes = 0
    num = i
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    if sum_of_cubes == i:
        print(i, end=" ")
print("\n")
# w.a.p to find a numbers is prime or not 
print("Prime numbers from 1 to 10:")
for i in range(1, 11):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, end=" ")
print("\n")
# w.a.p to find choice based calculator choice a numbers 
# 1=additions
# 2=multiplications
# 3=substraction
# 4=divisions
# 5=exit   
print("###################Calculator#################")
while True:
    print("1. Addition")
    print("2. Multiplication")
    print("3. Subtraction")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 5:
        print("Exiting the calculator.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        result = num1 + num2
        print("Result for addition:",result)
    elif choice == 2:
        result = num1 * num2
        print("Result for multiplication:",result)
    elif choice == 3:
        result = num1 - num2
        print("Result for subtraction:",result)
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("Result for division:",result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please try again.")

# create a list and iterate via for loop
print("Iterating through a list:")
print("List of numbers:")
numbers_list = [1, 2, 3, 4, 5]
for number in numbers_list:
    print(number, end=" ")
print("\n")
# create a dictionary and iterate via for loop
print("Iterating through a dictionary:")
student_scores = {
    "John": 24,
    "Steven": 45,
    "Alice": 67,
    "Bob":89
}
for student, score in student_scores.items():
    print("Student:", student,",", "Score:", score)
print("\n")
# create a tuple and iterate via for loop
print("Iterating through a tuple:")
numbers_tuple = (10, 20, 30, 40, 50)
for number in numbers_tuple:
    print(number, end=" ")