class calculator:
    """Perform operations between a vector and a scalar."""

    def __init__(self, vector):
        """Calculator constructor."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition between a vector and a scalar."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication between a vector and a scalar."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substraction between a vector and a scalar."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division between a vector and a scalar."""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
