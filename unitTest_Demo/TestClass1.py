import unittest
import selenium

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#" * 60)
        print("Class-1-> Class Level Setup (I will run only once before all tests)")
        print("*#" * 60)

    def setUp(self):
        print("Class-1-> I will run before every test ")

    def test_someRandomTestMethod1(self):
        print("Class-1-> Test-Method 1 run")

    def test_someRandomTestMethod2(self):
        print("Class-1-> Test-Method 2 run")

    def tearDown(self):
        print("Class-1-> I will run after every test ")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 60)
        print("Class-1-> Class Level TearDown (I will run only once after all tests )")
        print("*#" * 60)


if __name__ == '__main__':
    unittest.main(verbosity=2)
