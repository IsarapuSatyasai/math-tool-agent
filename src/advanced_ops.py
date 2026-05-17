import math
class AdvancedCalculator:
    """Handles advanced arithmetic operations."""
    
    def power(self, a: float, b: float) -> float:
        """Returns a raised to the power of b."""
        return a ** b
    
    def square_root(self, a: float) -> float:
        """Returns the square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return a ** 0.5
    
    def percentage(self, a: float, b: float) -> float:
        """Calculates what percentage a is of b."""
        if b == 0:
            raise ValueError("Cannot calculate percentage with a denominator of zero.")
        return (a / b) * 100
    
    def factorial(self, n: int) -> int:
        """Returns the factorial of n."""
        if n < 0:
            raise ValueError("Cannot calculate factorial of a negative number.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result