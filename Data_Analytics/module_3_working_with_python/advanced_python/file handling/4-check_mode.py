file = open("dictionary.txt","w")
if file:
    print("file opened successfully")
    # print mode
    print(file.mode)
    print(file.read)
    print(file.write)
else:
    print("file does not exist")