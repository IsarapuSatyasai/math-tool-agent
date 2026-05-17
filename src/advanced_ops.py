import math

class AdvancedCalculator:
    """Handles high-level mathematical operations."""
    
    def power(self, base: float, exponent: float) -> float:
        """Returns the result of base raised to the power of exponent."""
        return math.pow(base, exponent)
    
    def square_root(self, value: float) -> float:
        if value < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(value)

