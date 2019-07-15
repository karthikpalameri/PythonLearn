"""
imorting our own module and using its functions

our module : myPersonalModule
"""

# we are directly importing the require function only which is clean and fast and uses less memory
#    <directoryName.FileName> import <functionName>
from myPesonalModule.Cars import printInfo


class ownModuleImportDemo():

    def carDescription(self, make, model):
        printInfo(make, model)  # using the printInfo function which is present in myPersonalModule.Car


ownModuleImportDemo().carDescription("bmw", "m3")
