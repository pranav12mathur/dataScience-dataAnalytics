"""
# 1. Leap year

year = int(input("Enter year:"))
if(year%4==0 and year%100!=0) or(year%400==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
"""

"""
# 2. Positive or Negative Check
num = int(input("Enter the number:"))
if(num>0):
    print(num,"is positive")
else:
    print(num,"is negative")
"""

"""
#3. Admission Eligibility Check
marks =int(input("Enter marks:"))
if(marks>=300):
    print("Eligible for A batch")
elif(marks>=200):
    print("Eligible for B batch")
elif(marks>=100):
    print("Eligible for C batch ")
else:
    print("not eligible") 
"""
"""
#4. Temperature-Based Weather Message
temp = int(input("Enter temperature:"))
if(temp>=30):
    print("Weather is hot")
elif(temp>=10):
    print("Weather is normal")
else:
    print("Weather is cold")
"""

"""
# 5. Vowel or Consonant Check
word = str(input("Enter the word:"))
if(word=='a' or word=='e' or word=='i' or word=='o' or word=='u'):
    print(word ,"is a vowel" )
else:
    print(word ,"is a constonant")
"""

"""
# 6. Profit and Loss Calculation
bp = int(input("Enter buying price:"))
sp = int(input("Enter selling price:"))
profit = sp-bp
if(profit>=100):
    print("profit is huge")
elif(profit>=50):
    print("profit is good")
elif(profit>=10):
    print("profit is bad")
else:
    print("no profit")
"""
"""
#7. Geometrical Shapes Area Calculator
print("#############Shape Area Calculator############")
print("enter 1 for square")
print("enter 2 for circle")
print("enter 3 for triangle")
while True:
    choice = int(input("Enter choice:"))
    if(choice==1):
        s = int(input("Enter side:"))
        print("Area of square is:",s*s)
        break
    elif(choice==2):
        r = int(input("Enter radius:"))
        print("Area of circle is:",3.14*r*r)
        break
    elif(choice==3):
        b = int(input("Enter base:"))
        h = int(input("Enter height:"))
        print("Area of traingle is:",(b*h)/2)
        break
    else:
        print("invalid input")
        break
"""

"""
#8. Electricity Bill Calculator
units = int(input("Enter total units used:"))
if(units>=100):
    print("Bill is:",4*units)
elif(units>=50):
    print("Bill is:",3*units)
elif(units>=10):
    print("Bill is:",2*units)
else:
    print("No bill")
"""

"""
#9. Loan eligibility
credit_score = int(input("Enter your credit score:"))
monthly_income = int(input("Enter your monthly_income:"))
if credit_score>=700 and monthly_income>=30000:
    print("Loan approved")
else:
    print("Loan not approved")
"""

"""
#10. Scholarship check
marks = int(input("Enter your marks:"))
family_income = int(input("Enter your income:"))
if(marks>=75 and family_income<=30000):
    print("Eligible")
else:
    print("Not eligible")
"""