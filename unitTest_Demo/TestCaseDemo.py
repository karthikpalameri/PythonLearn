import unittest
import selenium

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#" * 60)
        print("I will run only once before all tests")
        print("*#" * 60)

    def setUp(self):
        print("I will run before every test ")

    def test_someRandomTestMethod1(self):
        print("Test-Method 1 run")

    def test_someRandomTestMethod2(self):
        print("Test-Method 2 run")

    def tearDown(self):
        print("I will run after every test ")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 60)
        print("I will run only once after all the tests")
        print("*#" * 60)


if __name__ == '__main__':
    unittest.main(verbosity=2)
