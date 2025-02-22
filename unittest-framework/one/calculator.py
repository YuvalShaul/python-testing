import unittest

# The class we want to test
class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Our test suite
class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This runs before each test
        self.calc = Calculator()
    
    def test_add(self):
        # Test basic addition
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
        
        # Test with negative numbers
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
    
    def test_divide(self):
        # Test basic division
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        
        # Test division by zero raises error
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()