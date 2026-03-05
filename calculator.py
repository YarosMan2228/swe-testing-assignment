class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, a: float, b: float) -> float:
        self.result = a + b
        return self.result

    def subtract(self, a: float, b: float) -> float:
        self.result = a - b
        return self.result

    def multiply(self, a: float, b: float) -> float:
        self.result = a * b
        return self.result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = a / b
        return self.result

    def clear(self) -> float:
        self.result = 0
        return self.result
