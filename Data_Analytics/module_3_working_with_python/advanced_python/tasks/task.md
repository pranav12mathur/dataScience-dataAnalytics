# 100 Practice Questions

## Section A: SQL (20 Questions)

### Basics (1–10)

1. What is SQL, and what is it used for?
```
SQL is a query language used for managing and manipulating relational databases. It allows users to create, read, update, and delete data in a structured format.
```
2. What is the difference between `DELETE`, `DROP`, and `TRUNCATE`?
```
- DELETE is used to remove specific rows from a table based on a condition, and it can be rolled back if within a transaction.
- DROP is used to remove an entire table or database, and it cannot be rolled back.
- TRUNCATE is used to remove all rows from a table and it cannot be rolled back, but it is faster than DELETE because it does not log individual row deletions.
```
3. Write a query to display all records from a table named `Students`.
```sql
select * from Students
```
4. Write a query to display only the `Name` and `Age` columns from the `Students` table.
```sql
select Name, Age from Students
```
5. How do you use the `WHERE` clause? Give an example.
```sql
-- WHERE clause is used to filter records based on a specified condition.
--example:
select * from Students where Age >= 18
```
6. Write a query to display students whose age is greater than 18.
```
select * from Students where Age > 18
```
7. What is the purpose of the `ORDER BY` clause?
```
ORDER BY clause is used to sort the columns in ascending  or descending order based on one or more columns.
```
8. Write a query to display students sorted by `Marks` in descending order.
```sql
select * from students order by Marks desc
```
9.  What is the difference between `DISTINCT` and `GROUP BY`?
```
- DISTINCT is used to return unique values from a column  
- GROUP BY is used to group rows that have the same values in specified columns.
```
10. Write a query to display unique city names from a `Students` table.
```sql
select distinct City from Students
```

### Intermediate (11–20)

11. What is the difference between `PRIMARY KEY` and `FOREIGN KEY`?
```
- PRIMARY KEY is a unique key that uniquely identifies each record in a table and cannot contain NULL values.
there can be only one primary key in a table.
- FOREIGN KEY is a key that references the primary key of another table to establish a relationship between the two tables. It can contain NULL values and there can be multiple foreign keys in a table.
```
12. Write a query to count the total number of students.
```sql
select count(*) from Students
```
13. Write a query to find the highest salary from an `Employees` table.
```sql
select max(Salary) from Employees
```
14. Write a query to calculate the average marks of students.
```sql
select avg(Marks) from Students
```
15. Explain the use of the `LIKE` operator with examples.
```sql
--The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
--Examples:
select * from Students where Name like '%B' 
select * from Students where Name like '%a%'
```
16. Write a query to display students whose names start with `'A'`.
```sql
select * from Students where Name like 'A%'
```
17. What is the purpose of the `JOIN` clause?
```
JOIN clause is used to combine rows from two or more tables based on a related column between them.
```
18. Explain the difference between `INNER JOIN` and `LEFT JOIN`.
```
- INNER JOIN returns only the rows that have matching values in both tables.
- LEFT JOIN returns all rows from the left table and the matched rows from the right table. If there is no match, NULL values are returned for columns from the right table.
```
19. Write a query to display employee names along with their department names using joins.
```sql
select e.Name, d.DepartmentName from employees e
inner join departments d on e.DepartmentID = d.DepartmentID
```
20. Write a query to find the second highest salary from an `Employees` table.
```sql
select salary from Employees order by Salary desc limit(1,1)
```
---

# Section B: IT Fundamentals (20 Questions)

1. What is a computer?
```
A computer is an electronic device that is used to perform various tasks such as calculations, data processing, and information storage. It consists of hardware and software components that work together to execute instructions and provide output.
```
2. Explain the difference between hardware and software.
```
- Hardware refers to the physical components of a computer system, such as the CPU, RAM, hard drive etc.
- Software refers to the programs and applications that run on a computer, enabling it to perform specific tasks. Examples include operating systems, word processors, and web browsers.
```
3. What are the different types of software?
```
The different types of software include:
- System software: Manages and operates computer hardware and provides a platform for other software to run (e.g., operating systems).
- Application software: Designed for specific tasks or user needs (e.g., word processors, web browsers).
- Programming software: Used by developers to write, test, and debug code (e.g., integrated development environments).
```
4. What is an operating system?
```
An operating system is system software that manages hardware and provides a platform for running applications.
It controls memory, processes, devices, and user interaction.
```
5. Name any five operating systems.
```
Examples of operating systems are Windows, macOS, Linux, Android, and iOS.
These are used on desktops, laptops, servers, and mobile devices.
```
6. What is RAM? How is it different from ROM?
```
RAM is volatile memory used for temporary data storage while the computer runs programs.
ROM is nonvolatile memory that stores firmware and retains data when power is off.
```
7. What is a CPU? Explain its main components.
```
The CPU is the central processing unit that executes instructions and controls computations.
Its main components are the arithmetic logic unit (ALU), control unit, and registers.
```
8. What is the function of the motherboard?
```
The motherboard connects and allows communication between CPU, memory, storage, and peripherals.
It houses the chipset, expansion slots, power connectors, and device interfaces.
```
9.  What is an IP address?
```
An IP address is a numeric label assigned to each device on a network for identification and routing.
It enables devices to send and receive data over the internet or local networks.
```
10. What is the difference between LAN, MAN, and WAN?
```
LAN is a local area network covering a small area like a home or office.
MAN covers a city and WAN covers wide geographic areas, connecting multiple LANs.
```
11. What is cloud computing?
```
Cloud computing delivers computing services like storage, databases, and applications over the internet.
Users access resources on demand without managing physical hardware.
```
12. Explain the difference between HTTP and HTTPS.
```
HTTP is an unsecured protocol for transferring web data.
HTTPS adds encryption with SSL/TLS to secure data between browser and server.
```
13. What is a database?
```
A database is an organized collection of structured data stored and managed for efficient retrieval.
It allows users and applications to query, insert, update, and delete information.
```
14. What is the difference between primary storage and secondary storage?
```
Primary storage like RAM is fast and directly accessible by the CPU but volatile.
Secondary storage like HDDs and SSDs is nonvolatile and used for long-term data retention.
```
15. What is a firewall?
```
A firewall is a security system that monitors and controls incoming and outgoing network traffic.
It blocks unauthorized access and allows trusted communication based on rules.
```
16. What is antivirus software?
```
Antivirus software detects, prevents, and removes malware from computers.
It scans files, monitors behavior, and helps protect the system from infections.
```
17. Explain the difference between compiler and interpreter.
```
A compiler translates the entire source code into machine code before execution.
An interpreter converts and executes code line by line at runtime.
```
18. What is the difference between the Internet and the World Wide Web?
```
The Internet is the global network of connected computers and infrastructure.
The World Wide Web is a service on the Internet for accessing linked documents via browsers.
```
19. What is phishing?
```
Phishing is a cyberattack where attackers fake trustworthy communication to steal sensitive data.
It often uses emails or websites to trick users into revealing passwords or financial information.
```
20. Explain the booting process of a computer.
```
Booting starts when the computer powers on, runs firmware checks, and loads the operating system.
The BIOS/UEFI initializes hardware, then the OS kernel takes over and starts system services.
```

---

# Section C: Python Task-Based Questions (60 Questions)

## Operators (1–10)

1. Write a program to add two numbers.
```python
x = 5
y = 6
print("Addition:",x+y)
```
2. Write a program to find the largest of two numbers using comparison operators.
```python
x = 5
y = 10
if(x>y):
    print("x is greater")
else:
    print("y is greater")
```
3. Write a program to swap two variables without using a third variable.
```python
x = 4
y = 5
print("Before swap: x = ",x,"y = ",y)
x = x+y
y = x-y
x = x-y
print("After swap: x = ",x,"y = ",y)
```
4. Write a program to calculate the area of a rectangle.
```python
l = 5
b = 4
area = l*b
print("Area of rectangle:",area)
```
5. Write a program to check whether a number is even or odd.
```python
x = 4
if(x%2==0):
    print("Number is even")
else:
    print("Number is odd")
```
6. Write a program to calculate simple interest.
```python
p = 1000
r = 5
t = 10
si = (p*r*t)/100
print("Simple interest is:",si)
```
7. Write a program to convert Celsius to Fahrenheit.
```python
C = 45
F = (C*1.8)+32
print("Temperature in Fahrenheit is:",F)
```
8. Write a program to calculate the square and cube of a number.
```python
import math
x = 2
print("Square is:",math.pow(x,2))
print("Cube is:",math.pow(x,3))
```
9. Write a program to calculate the remainder when one number is divided by another.
```python
x = 10
y = 6
print("Reaminder is:",x%y)
```
10. Write a program to check whether a number is divisible by both 3 and 5.
```python
x = 15
if(x%3==0 and x%5==0):
    print("Number is both divisible by 3 and 5")
elif(x%3==0 and x%5!=0):
    print("Number is divisible by 3 but not by 5")
elif(x%3!=0 and x%5==0):
    print("Number is divisible by 5 but not by 3")
else:
    print("Number is not divisible by both 3 and 5")
```

## Functions (11–20)

11. Create a function to add two numbers.
```python
def add(a,b):
    return a+b
print("Addition:",add(2,3))
```
12. Create a function to calculate the factorial of a number.
```python
def fact(n):
    x = 1
    for i in range(1,n+1):
        x *=i
    return x
print("Factorial is:",fact(5))
```
13. Write a function to check whether a number is prime.
```python
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = 2
if is_prime(n):
    print("Number is prime")
else:
    print("Number is not prime")
```
14. Create a function to find the largest of three numbers.
```python
def large_among_three(x,y,z):
    if(x>y and x>z):
        print(x," is the larger number")
    elif(y>z and y>x):
        print(y," is the larger number")
    else:
        print(z," is the larger number")
large_among_three(3,2,5)
```
15. Write a function to count vowels in a string.
```python
def count_string(name):
    count = 0
    vowels = "aeiouAEIOU"
    for char in name:
        if char in vowels:
            count+=1
    return count
print("Total vowel count:",count_string("Ashley"))
```
16. Create a function to reverse a string.
```python
def reverse_string(name):
    return name[::-1]
print("Reversed string is:",reverse_string("John"))
```
17. Write a function to calculate the square of a number.
```python
def square(n):
    return n*n
print("Square is:",square(5))
```
18. Create a function to return the sum of elements in a list.
```python
def sum_list(lst):
    return sum(lst)
print("Sum of list is:",sum_list([1, 2, 3, 4, 5]))
```
19. Write a function to find the maximum number in a list.
```python
def max_list(lst):
    return max(lst)
print("Maximum number in list is:",max_list([1, 2, 3, 4, 5]))
```
20. Create a function that accepts a name and prints a greeting message.
```python
def greet(name):
    print("Hello, " + name + "!")
greet("Vince")
```

## Lists (21–30)

21. Create a list of five numbers and print it.
```python
numbers = [1,2,3,4,5]
print(numbers)
```
22. Add an element to a list.
```python
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
```
23. Remove an element from a list.
```python
numbers = [1,2,3,4,5]
numbers.pop(2)
print(numbers)
```
24. Find the largest element in a list.
```python
numbers = [1,2,3,4,5]
print(max(numbers))
```
25. Find the smallest element in a list.
```python
numbers = [1,2,3,4,5]
print(min(numbers))
```
26. Calculate the sum of all elements in a list.
```python
numbers = [1,2,3,4,5]
print(sum(numbers))
```
27. Count how many times an element appears in a list.
```python
numbers = [1,2,3,4,5]
print(len(numbers))
```
28. Reverse a list.
```python
numbers = [1,2,3,4,5]
print(numbers[::-1])
```
29. Sort a list in ascending order.
```python
numbers = [5,2,3,1,4]
print(sorted(numbers))
```
30. Remove duplicate elements from a list.
```python
numbers = [1,2,3,4,5,1,2,3]
print(list(set(numbers)))
```

## Tuples and Strings (31–40)

31. Create a tuple of five numbers.
```python
numbers = (1,2,3,4,5)
print(numbers)
```
32. Access the third element of a tuple.
```python
numbers = (1,2,3,4,5)
print(numbers[2])
```
33. Count occurrences of an element in a tuple.
```python
numbers = (1,2,2,3,2)
print(numbers.count(2))
```
34. Find the index of an element in a tuple.
```python
numbers = (1,2,3,4,5)
print(numbers.index(4))
```
35. Reverse a string.
```python
text = "hello"
print(text[::-1])
```
36. Count the number of vowels in a string.
```python
text = "hello world"
print(sum(1 for c in text.lower() if c in "aeiou"))
```
37. Check whether a string is a palindrome.
```python
text = "madam"
print(text == text[::-1])
```
38. Convert a string to uppercase.
```python
text = "hello"
print(text.upper())
```
39. Replace all spaces in a string with hyphens.
```python
text = "hello world"
print(text.replace(" ", "-"))
```
40. Count the number of words in a sentence.
```python
sentence = "hello world"
print(len(sentence.split()))
```

## Conditional Statements (41–50)

41. Check whether a number is positive, negative, or zero.
```python
n = 5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
42. Find the largest of three numbers.
```python
a = 5
b = 10
c = 3
if a > b and a > c:
    print("a is largest")
elif b > c and b>a:
    print("b is largest")
else:
    print("c is largest")
```
43. Check whether a year is a leap year.
```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```
44. Check whether a person is eligible to vote.
```python
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```
45. Calculate grades based on marks.
```python
marks = 85
if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "F"
print(grade)
```
46. Check whether a character is a vowel or consonant.
```python
ch = "a"
if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")
```
47. Create a simple calculator using `if-elif`.
```python
a, b, op = 5, 2, "*"
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("invalid")
```
48. Check whether a number is divisible by 7.
```python
n = 14
if n % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")
```
49. Find whether a number is a multiple of 10.
```python
n = 30
if n % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")
```
50. Check whether a student has passed (marks >= 35).
```python
marks = 40
if marks >= 35:
    print("Student has passed")
else:
    print("Student has failed")
```

## Loops and File Handling (51–60)

51. Print numbers from 1 to 100 using a `for` loop.
```python
for i in range(1, 101):
    print(i)
```
52. Print the multiplication table of a given number.
```python
n = 5
for i in range(1, 11):
    print(n, "*", i, "=", n * i)
```
53. Find the sum of numbers from 1 to `N`.
```python
N = 10
print(sum(range(1, N + 1)))
```
54. Print all even numbers between 1 and 100.
```python
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
```
55. Print the Fibonacci series up to `N` terms.
```python
N = 10
a, b = 0, 1
for _ in range(N):
    print(a)
    a, b = b, a + b
```
56. Find the factorial of a number using a loop.
```python
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```
57. Count the number of digits in a number.
```python
n = 12345
print(len(str(abs(n))))
```
58. Create a text file and write your name, age, and city into it.
```python
with open("info.txt", "w") as f:
    f.write("Name: Pranav, Age: 22, City: Ajmer")
```
59. Read data from a text file and display it.
```python
with open("info.txt", "r") as f:
    print(f.read())
```
60. Count the number of words and lines in a text file.
```python
with open("info.txt", "r") as f:
    lines = f.readlines()
print("Lines:", len(lines))
print("Words:", sum(len(line.split()) for line in lines))
```

---

## Summary

| Section | Questions |
|---------|----------:|
| SQL | 20 |
| IT Fundamentals | 20 |
| Python (Task-Based) | 60 |
| **Total** | **100** |