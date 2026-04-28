def square(x: int | float) -> int | float:
    """Square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """x to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer docstring."""
    count = 0

    def inner() -> float:
        """inner docstring."""
        nonlocal x
        nonlocal count
        count = function(x)
        x = count
        return count

    return inner
