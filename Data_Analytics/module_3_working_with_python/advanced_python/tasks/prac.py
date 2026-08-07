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