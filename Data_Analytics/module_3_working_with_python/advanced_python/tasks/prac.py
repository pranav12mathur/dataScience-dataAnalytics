num = int(input("Enter a number: "))
even_count = 0
odd_count = 0
if(num%2==0):
    even_count += 1
else:
    odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)