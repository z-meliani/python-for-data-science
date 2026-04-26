class calculator:
    """Perform operations between 2 vectors of same size."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors."""
        print("Dot product is:", sum([x * y for x, y in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two vectors."""
        print("Add Vector is :", [float(x + y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction of two vectors."""
        print("Sous Vector is :", [float(x - y) for x, y in zip(V1, V2)])
