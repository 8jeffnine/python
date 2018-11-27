# import statement
import unittest

class HelloWorldUnitTest(unittest.TestCase):
    def testCase(self):
        result = 1
        expected = 1
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()


# 1) import unittest
# 2) make class
# 3) make function
# 4) run the tests