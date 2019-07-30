import unittest

from unitTest_Demo import TestClass1
from unitTest_Demo import TestClass2

# get all tests from testclass1 and testclass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create a testsuite combinng testclass1 and testclass2
smoke_test = unittest.TestSuite([tc1, tc2])
smoke_test.addTest(TestClass1.TestClass1("sdf"))

unittest.TextTestRunner().run(smoke_test)
