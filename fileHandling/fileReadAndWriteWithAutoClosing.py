
def someMethod():
    print("with.. as.. Write operaion")
    with open("WriteAndReadFile.txt","w") as filWriteRef:
        filWriteRef.write("This is an example of with as Write operation")

    print()

    print("with.. as.. Read Operation")
    with open("WriteAndReadFile.txt","r+") as filReadRef:
        print(str(filReadRef.read()))


someMethod()