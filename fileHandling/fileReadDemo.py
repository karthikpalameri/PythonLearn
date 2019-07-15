my_readFileRef = open("readFile.txt", "r")

print(my_readFileRef.read())  # will read the whole file

my_readFileRef.close()

my_readFileRef = open("readFile.txt", "r")
print("Read lineByline->")
print(my_readFileRef.readline())

