# open()
file = open("hello.txt","r")
if file:
    print("file is opened successfully")
else:
    print("something went wrong")

file.close()