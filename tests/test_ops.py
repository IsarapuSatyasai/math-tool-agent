import unittest
from src.core_ops import CoreCalculator

class TestCoreCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = CoreCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)


if __name__ == "__main__":
    unittest.main()