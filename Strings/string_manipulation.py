from builtins import print, set

Str = "something is  \"fagfag\" "
first="nyc test temp"[5:-5]

second=Str[0]

print(Str)
print(first)
print(second)

"""
STRING FUNCITONS 
len()
lower()
upper()
str()
"""


stri="this is MiXed Case"

print("**************************************")
print("converting to lower case:"+stri.lower())
print("converting to Upper case:"+stri.upper())
print("len(str) and converting it to string " + str(len(stri)))

"""
String concatination 
"""

print("concatinating->""hell"+" "+"world")

"""
string replace
"""
print("string replace...")
a="1abc2abc3abc4abc"
print("a->"+a)
print("Replacing 1st 2 instance only using a.replace(\"abc\",\"xyz\",2) ->"+a.replace("abc","xyz",2))
print("Replacing all instance  using a.replace(\"abc\",\"xyz\",-1) ->"+a.replace("abc","xyz",-1))


"""
Sub-String
"""
print("Sub-String...")
a="1abc2abc3abc4abc"
  #0123456789
print("a->"+a)
print("Substing a[0]->"+a[0])
print("Substing a[-1] will print last chatacter->"+a[-1])
print("Substing a[1:5] will print from 1st index chatacter to 4th index character leaving the 5th index character->"+a[1:5])

"""
Sub-String with step
Starting index is inclusive 
Ending index is exclusive 
"""
print("Sub-String with STEP...")
print("a->"+a)
print("Substing with STEP a[1:5:1]->"+a[1:5:1])
print("Substing with STEP a[1:5:2]->"+a[1:5:2])
print("Substing with STEP a[1:5:3]->"+a[1:5:3])

"""
Slicing
slicing is quick and used in lot of programming 
"""
print("Slicing...")
a="This Is A Sting"
print("a->"+a)
print("Slicing with a[:]->"+a[:])
print("Slicing with a[1:]->"+a[1:])
print("Slicing with a[:6]->"+a[:6])
print("Slicing with a[len(a)-1]->"+a[len(a)-1])
print("Slicing with a[-1]->"+a[-1])
print("Slicing with a[-2]->"+a[-2])
print("Slicing with steps...")
print("a->"+a)
print("Slicing with Steps a[::1]->"+a[::1])
print("Slicing with Steps a[::2]->"+a[::2])
print("STRING REVERSE || Slicing with Steps a[::-1]->"+a[::-1])
print("Slicing with Steps a[::-2]->"+a[::-2])
print("String are immutable . It does not store after manipulating->"+a[0])
"""
we cant do a[0]="x" because strings 
"""

"""
String Formatting 
"""
print("String Formatting ...")
city = "nyc"
event = "show"
print("welcome to "+city+"and enjoy the "+event)
#print with
print("welcome to %s and enjoy the %s" %(city,event))


"""
LISTS
"""
print("*"*60)
print("List...")
cars = ["benz", "honda", "audi"]
empty_list = []
print(empty_list)

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]
print("".join(str(num_list)))
print(" Sum of first two values in the list->"+str(sum_num))



print("cars -> %s"%(cars))
cars[0] = "bmw"
print("Assigning bmw to index 1 and replacing benz, cars[1]=\"bmw\" -> %s" %(cars))


"""
Printing a list
"""
print("*"*60)
print("printing a list using for loop->")
for x in range(len(cars)):
    print (cars[x])

print("printing a list using loops printing  the list using * operator seperated by space  print(*cars) ->")
print(*cars)

print("printing a list using loops printing  the list using * operator seperated by comma  print(*cars, sep=", ") ->")
print(*cars, sep=", ")

print("printing a list using loops printing  the list using * operator seperated by \n  print(*cars, sep=", ") ->")
print(*cars, sep="\n")

print("printing the list using join function \" \".join(cars)->"+" ".join(cars))
print("printing the list using join function \" \".join(cars)->"+"-".join(cars))

