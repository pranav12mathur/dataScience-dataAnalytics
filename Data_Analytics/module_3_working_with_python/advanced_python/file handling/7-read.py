file = open("dictionary.txt","r")
# read a file
res = file.read()
print(res)
print("File read successfully")
file.close()