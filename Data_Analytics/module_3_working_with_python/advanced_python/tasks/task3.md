# wap to print star pattern

```python
for i in range(1, 6):
    print("*" * i)
```

# wap from 1 to 10 and find only even numbers between 1 to 10

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

# wap to print multiplication of tables

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()
```

# wap to print find sum of numbers from 1 to 100

```python
total = 0
for i in range(1, 101):
    total += i
print(total)
```

# wap to reverse a string

```python
s = "Hello, World!"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)
```

# wap to find sum list of elements

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print(total)
```

# wap to find largest no.s in a list

```python
numbers = [1, 2, 3, 4, 5]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(largest)
```

# wap to print a numbers from 10 to 1 using while loop

```python
i = 10
while i >= 1:
    print(i)
    i -= 1  
```

# wap to sum of digits using while loop

```python
sum = 0
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(sum)
```

# wap to count digits take input from users

```python
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)
```

# wap to print star reverse pattern 

```python
for i in range(5, 0, -1):
    print("*" * i)
```

# wap to make a password login authentication system if user input correct password it's authenticated login successfully otherwise in correct password if user continue enter 3 attempts failed your account will be blocked

```python
print("Welcome to the login system.")
password = "secret123"
attempts = 0
while attempts < 3:
    user_password = input("Enter password: ")
    if user_password == password:
        print("Login successful.")
        break
    else:
        print("Incorrect password.")
        attempts += 1
if attempts == 3:
    print("Your account has been blocked.")
```
# wap to count even and odd number

```python
num = int(input("Enter a number: "))
even_count = 0
odd_count = 0
if(num%2==0):
    even_count += 1
else:
    odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)
```

# find a smallest number in any given list
```python
numbers = [5, 2, 9, 1, 5, 6]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print(smallest)
```