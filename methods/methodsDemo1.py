"""
methods demo

A group of code statements which can perform same specific task
Methods are reusable and can be called when needed in the code

def
"""


def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return (n1 + n2)


sum1 = sum_nums(2, 8)
sum2 = sum_nums(3, 3)
stringAdd = sum_nums('one', 'two')
print("Sum1 ->{} ".format(sum1))
print("Sum2 ->{} ".format(sum2))
print("stringAdd ->{} ".format(stringAdd))

"""
Find if the passed value in the list 
"""
print("*" * 60)
print("check if it is in the list..")


def isMetro(city):
    l = ['sfo', 'nyc', 'la']
    if city in l:
        return True
    :
        return False


print(isMetro("nyc"))

"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from the outside
"""
print("*" * 60)
print("Positional parameter..")


def sum_nums2(n1=2, n2=4):
    """
    Get sum of numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


print("sum_nums2()  returned ->", sum_nums2())
print("sum_nums2(6,4)  returned ->", sum_nums2(6, 4))
print("sum_nums2(n1=8,n2=3)  returned ->", sum_nums2(n1=8, n2=3))
print("sum_nums2(n1=8,n2=3)  returned ->", sum_nums2(n1=8, n2=3))
# If you change the positon of the parameter while passing it will go and assign to the exact specified parameter (positon doesnt matter)
print("sum_nums2(n2=4,n1=5)  returned ->", sum_nums2(n2=4, n1=5))

"""
Variable Scope
local 
global
"""
print("*" * 60)
print("Local Variable Scope Demo..")

a = 10


def someMethod(a):
    print("The value of local variable a ->{}".format(a))
    a = 2
    print("The value of local variable a ->{}".format(a))


print("Value of global variable a ->{}".format(a))
someMethod(a)
print("Did the value of global variable change ? ->{}".format(a))
"""
Global Variable Scope
"""
print("*" * 60)
print("Global variable Scope..")

x = 10


def someOtherMethod():
    global x
    print("The value of 'x' inside the method ->{}".format(x))
    x = 9
    print("The value of 'x' inside the method ->{}".format(x))


print("Value of global variable 'x' ->{}".format(x))
someOtherMethod()
print("Did the value of global 'x' change ? ->{}".format(x))

"""
Some built-in functions
max():

min():

abs():

type():

"""


def largest_num(*args):
    print("Largest number among is->")
    return (max(args))


largest_num(-34, 50, 46, 4343, 3, -2)


def smallest_num(*args):
    print("Smallest number among is->")
    return (min(args))


smallest_num(34, 54, 75, 34, 234, 62, 0, -44)


def abs_funtion(a):
    print("abs is ->{}".format(a))


abs_funtion(-40)
abs_funtion(+40)

print(type(1))
print(type(99.9))
print(type("something"))
lis = ['a', 0.99, 4, -5, 0.5]
print(type(lis))
