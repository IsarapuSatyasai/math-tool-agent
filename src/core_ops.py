class CoreCalculator:
    """Handles basic arithmetic operations."""
    
    def add(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b
    
    def modulus(self, a: float, b: float) -> float:
        """Calculates the modulus of a by b."""
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b