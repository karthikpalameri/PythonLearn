"""
Inheritence
"""


class Car(object):

    def __init__(self):
        print("Car class instance just created (constructor)")

    def carStart(self):
        print("Car Started")

    def carStop(self):
        print("Car Stop")


class Bmw(Car):
    def __init__(self):
        print("You just created the BMW instance")

    def carStart(self):  # method overriding
        super().carStart() #calling parent class method 
        print("Bmw CAr start..")

    def headsUpDisplay(self):
        print("Bmw Heads Up Display implementaion")


carObject = Car()
carObject.carStart()
carObject.carStop()

bmwObject = Bmw()
bmwObject.carStart()
bmwObject.headsUpDisplay()
bmwObject.carStop()
