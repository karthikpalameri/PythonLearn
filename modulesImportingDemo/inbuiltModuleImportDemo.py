"""
https://www.docs.python.org/3/library
"""

import math
from math import sqrt

class inbuiltModuleImportDemo():

    def buitInModules(self):
        print(math.sqrt(100)) #accessing using importing the whole modules which takes lot of time to import
        print(sqrt(25))#accessing only the sqrt function id fast and uses less memory

m= ModuleDemo()
m.buitInModules()