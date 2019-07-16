"""
Object Oriented programming
"""


class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def printInfo(self):
        print("*"*60)
        print("Make of the car is -> "+self.make)
        print("Model of the car is -> "+ self.model)

c1 = Car("bmw", '550i')
c1.printInfo()

c2 = Car("benz", 'E350')
c2.printInfo()
