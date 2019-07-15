class Fruit(object):
    def __init__(self):
        print("This is Fruit class constructor")

    def nutrition(self):
        print("Fruit class nutrition method")

    def shap(self):
        print("Fruit can have any shape")


class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("Apple fruit class constructor")

    def nutrition(self):
        print("Apple nutrition")

    def shap(self):
        print("Apple shape")


f = Fruit()
f.nutrition()
f.shap()

a = Apple()
a.nutrition()
a.shap()
