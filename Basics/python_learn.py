from builtins import print

Str = "something is  \"fagfag\" "
first = "nyc test temp"[5:-5]

second = Str[0]

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

stri = "this is MiXed Case"

print("**************************************")
print("converting to lower case:" + stri.lower())
print("converting to Upper case:" + stri.upper())
print("len(str) and converting it to string " + str(len(stri)))

"""
String concatination 
"""

print("concatinating->""hell" + " " + "world")

"""
string replace
"""
print("string replace...")
a = "1abc2abc3abc4abc"
print("a->" + a)
print("Replacing 1st 2 instance only using a.replace(\"abc\",\"xyz\",2) ->" + a.replace("abc", "xyz", 2))
print("Replacing all instance  using a.replace(\"abc\",\"xyz\",-1) ->" + a.replace("abc", "xyz", -1))

"""
Sub-String
"""
print("Sub-String...")
a = "1abc2abc3abc4abc"
# 0123456789
print("a->" + a)
print("Substing a[0]->" + a[0])
print("Substing a[-1] will print last chatacter->" + a[-1])
print(
    "Substing a[1:5] will print from 1st index chatacter to 4th index character leaving the 5th index character->" + a[
                                                                                                                     1:5])

"""
Sub-String with step
Starting index is inclusive 
Ending index is exclusive 
"""
print("Sub-String with STEP...")
print("a->" + a)
print("Substing with STEP a[1:5:1]->" + a[1:5:1])
print("Substing with STEP a[1:5:2]->" + a[1:5:2])
print("Substing with STEP a[1:5:3]->" + a[1:5:3])

"""
Slicing
slicing is quick and used in lot of programming 
"""
print("Slicing...")
a = "This Is A Sting"
print("a->" + a)
print("Slicing with a[:]->" + a[:])
print("Slicing with a[1:]->" + a[1:])
print("Slicing with a[:6]->" + a[:6])
print("Slicing with a[len(a)-1]->" + a[len(a) - 1])
print("Slicing with a[-1]->" + a[-1])
print("Slicing with a[-2]->" + a[-2])
print("Slicing with steps...")
print("a->" + a)
print("Slicing with Steps a[::1]->" + a[::1])
print("Slicing with Steps a[::2]->" + a[::2])
print("STRING REVERSE || Slicing with Steps a[::-1]->" + a[::-1])
print("Slicing with Steps a[::-2]->" + a[::-2])
print("String are immutable . It does not store after manipulating->" + a[0])
"""
we cant do a[0]="x" because strings 
"""

"""
String Formatting 
"""
print("String Formatting ...")
city = "nyc"
event = "show"
print("welcome to " + city + "and enjoy the " + event)
# print with
print("welcome to %s and enjoy the %s" % (city, event))

"""
LISTS
"""
print("*" * 60)
print("List...")
cars = ["benz", "honda", "audi"]
empty_list = []
print(empty_list)

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]
print("".join(str(num_list)))
print(" Sum of first two values in the list->" + str(sum_num))

print("cars -> %s" % (cars))
cars[0] = "bmw"
print("Assigning bmw to index 1 and replacing benz, cars[1]=\"bmw\" -> %s" % (cars))

"""
Printing a list
"""
print("*" * 60)
print("printing a list using for loop->")
for x in range(len(cars)):
    print(cars[x])

print("printing a list using loops printing  the list using * operator seperated by space  print(*cars) ->")
print(*cars)

print("printing a list using loops printing  the list using * operator seperated by comma  print(*cars, sep=", ") ->")
print(*cars, sep=", ")

print("printing a list using loops printing  the list using * operator seperated by \n  print(*cars, sep=", ") ->")
print(*cars, sep="\n")

print("printing the list using join function \" \".join(cars)->" + " ".join(cars))
print("printing the list using join function \" \".join(cars)->" + "-".join(cars))

print("*" * 60)
print("List now is -> %s" % (cars))

print("Length of the list now is -> %s" % (len(cars)))
temp = "xyz"
print("Temp is ->" + temp)
cars.append(temp)
print("Appending value \"{}\" to the end of the list, List now is -> {} ".format(temp, cars))

cars.insert(1, "abc")
print("Inserted a value to the 1st index -> {}".format(cars))

index = cars.index("bmw")
print("Getting the index -> {}".format(index))

popped_item = cars.pop()
print("Popped \"{}\" from the list and list now is -> {} ".format(popped_item, cars))

cars.remove("abc")
print("After removing it doesnt return the value . Now the list is ->", cars)

print(cars)

slicing = cars[0:2]
print(slicing)

a = cars[1:]
print(a)

cars.sort()
print("Sorted list is ", cars)

"""
Dictonary
"""

print("*" * 60)
print("Dictonary..")

car = {"make": "bmw", "model": "550i", "year": 2016}
print(car)
model = car["model"]
print(car["year"])
print(model)

d = {}
# adding key value to empty dictonary
d['one'] = 1
d['two'] = 2
print(d)

sum_1 = d['two'] + 8
print(sum_1)

# changing the value of the dictonary on the fly

d['two'] = d['two'] + 8
print(d)

"""
Nested Disctonary
"""
print("*" * 60)
print("Nested Dictonary..")

d = {'k1': {"nestk1": "nestkeyvalue1", "nestk2": "nestvalue2"}}
print(d)

cars = {'bmw': {'model': "550i", 'year': 2016}, 'benz': {'model': "E350", 'year': 2015}}
print(cars)

# Accessing the Nested Dictonary
bmw_year = cars["bmw"]["year"]
print(bmw_year)
print("Getting the benz year -> {}".format(cars["benz"]["year"]))

"""
 Dictonary methods 
"""
print("*" * 60)
car = {"make": "bmw", "model": "550i", "year": 2016}

cars = {'bmw': {'model': "550i", 'year': 2016}, 'benz': {'model': "E350", 'year': 2015}}

print(car)
print(cars)
print(car.keys())
print(cars.keys())

print(car.values())
print(cars.values())

print(car.items())

car_copy = car.copy()
print(car_copy)

car_copy.clear()
print(car_copy)

print(car)
print(car.pop("model"))

print(car)

"""
 Tuple
 Like list but Immuutable
 It means you cant change them
 
 somemethods are 
 .index
 .count(1)
 
"""

print("*" * 60)
print("Tuple..");

print("List example")
my_list = [1, 2, 3]
print(my_list)

my_list[0] = 0
print(my_list)

print("Tuple example")
my_tuple = (1, 2, 3, 4, 5, 9, 9)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0]=9

print(my_tuple)
print(my_tuple[0])

print(my_tuple[1:])

print(my_tuple.index(3))

print("Counts the number of times the {} is present -> {}".format(9, my_tuple.count(9)))

"""
Comparators
==
!=
>
<
>=
<=

"""
print("*" * 60)
print("Comparators..")

bool_1 = 10 >= 11 - 1
print(bool_1)

"""
and 

T and T -> True
T and F -> F
F and F -> F


or 
T or T -> T
T or F -> T
F or F -> F


not
Not T -> F
Not F -> T

"""

and_1 = (1 == 1) and (2 > 1)
print(and_1)

or_l = (1 == 1) or (2 == 3)
print(or_l)

not_1 = not (1 == 1)
print(not_1)

"""
Order oof precedence 
braces first 
1.not
2.and
3.or
"""

bool_2 = True or not False and False
print(bool_2)

bool_3 = (1 == 1 or not 1 > 1) and 1 > 1
print(bool_3)

"""
Conditional logic 
"""
print("*" * 60)
print("Conditional logic..")

if (1 == 1):
    print("Is equal")

print("Not in if block because its not it indentation")

value = 'red'

if value == 'red':
    print("red")
elif value == 'yellow':
    print("yellow")
else:
    print("not red")

"""
Loops

While 


Iterable items are Strings , List , Tuple , Dictonary 

"""
print("*" * 60)
print("Loops..")

x_1 = 0
while x_1 < 10:
    print("value of x is : " + str(x_1))
    x_1 = x_1 + 1

listy = []

y = 1
while y < 10:
    listy.append(y)
    print("value of y is : " + str(y))
    y = y + 1

print(listy)

print("*" * 60)
print("While Break Continue..")

print("*" * 60)
z = 0
while z < 10:

    z = z + 1
    print("Value of z is :" + str(z))

    if z > 5:
        print("Value of z is {} so Contining without executing the below staments in  loop".format(z))
        continue

    if z == 10:
        print("Value of z is {} so Breaking out of the while loop".format(z))
        break

    print("Continuing inside the loop")
    print("*" * 60)

print("Just broke out of the loop")

"""
If Break is applied it will break out of the  block also so keep in mind 
"""
p = 0
print("*" * 60)
print("While loop demo with  block ")
while p < 15:
    p = p + 1
    print("Value of z is :" + str(z))
    # if p==10:
    #     print("Value of z is {} so Breaking out of the while loop".format(z))
    #     break
    print("Continuing inside the loop")
    print("*" * 60)
else:
    print(
        "Just broke out of the loop and Entering the Else block of the while loop after the while loop is executed completely")

m = 0
print("*" * 60)
print("While loop demo with Else block and Break STatements skipping the else block ")
while m < 15:
    m = m + 1
    print("Value of z is :" + str(z))
    if m == 10:
        print("Value of m is {} so Breaking out of the while loop".format(z))
        break
    print("Continuing inside the loopp")
    print("*" * 60)
# else:
#     print(
#         "Just broke out of the loop and Entering the Else block of the while loop after the while loop is executed completely")


print("Printing this line as the flow is out of the while loop ")

"""
For Loop
"""

print("*" * 60)
print("For Loop")

temp_string = "abcabc"

for c in temp_string:
    print(c, end='-')

print("\n")
print("*" * 60, end='\n')

# String for loop
print("String For loop..")
for c in temp_string:
    if not c.isupper():
        print(c.upper(), end='-')

print()
print("*" * 60, end='\n')

# List for loop
print("List For loop..")
temp_listt = [1, 2, 3]
for listitems in temp_listt:
    print(listitems * 10, end=" endd\n")

print()
print("*" * 60, end='\n')

# Dictonary for loop
print("Dictonary For loop..")
d_temp = {'one': 1, 'two': 2, 'three': 3}
for k in d_temp:
    print(k + " " + str(d_temp[k]))

print()
print(d_temp.items())

# Dictonary 2 for loop #iterate all the key and value
for k, v in d_temp.items():
    print("Key->{} value->{}".format(k, v))

"""
Zip MultipleList , Iterating multiple list at the same time will exhaust if the any list ends 
"""

list1 = [1, 2, 3, 9]
list2 = [6, 7, 8, 0, 4, 5]

for list1, list2 in zip(list1, list2):
    if (list1 > list2):
        print(list1)
    else:
        print(list2)

"""
Built in function 
Create  a sequence of number but doesnt save them in the memory 
Very useful for generating numbers
range(0,10)
"""
print("*" * 60, end='\n')
print("Range function..")

# printing range from 0 to 9 , 10 is excluded
print(list(range(0, 10)))

a = range(0, 10)
print(a)
print(type(a))
print(list(a))

# printing without the start so it prints upto 29 from 0
print(list(range(30)))

# printing even number by using the step in range function
print(list(range(0, 10, 2)))


