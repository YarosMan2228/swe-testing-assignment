"""
Quick-Calc: Core calculator logic.

This module provides the Calculator class with four basic operations
and a clear/reset function.
"""


class Calculator:
    """A simple calculator that supports add, subtract, multiply, divide, and clear."""

    def __init__(self):
        self.result = 0

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        self.result = a + b
        return self.result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a minus b."""
        self.result = a - b
        return self.result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        self.result = a * b
        return self.result

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = a / b
        return self.result

    def clear(self) -> float:
        """Reset the stored result to zero and return 0."""
        self.result = 0
        return self.result
