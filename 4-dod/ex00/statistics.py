
def ft_mean(*args: int | float) -> int | float:
    """Compute the mean of arguments."""

    return sum(args) / len(args)


def ft_median(*args: int | float) -> int | float:
    """Compute the median of arguments."""

    lst = sorted(args)
    n = len(lst)
    mid = n // 2

    if n % 2 == 0:
        return (lst[mid] + lst[mid + 1]) / 2

    return lst[mid]


def ft_quartile(*args: int | float) -> list[float]:
    """Compute the quartiles (Q1, Q3) of arguments."""

    lst = sorted(args)
    n = len(lst)
    pos = [(n - 1) * p for p in [0.25, 0.75]]

    qn = []
    for i in pos:
        low = int(i)
        high = min(low + 1, n - 1)
        qn.append(lst[low] + (lst[high] - lst[low]) * (i - low))

    return qn


def ft_var(*args: int | float) -> float:
    """Compute the variance of arguments."""

    mean = sum(args) / len(args)
    n = len(args)

    return (sum([(x - mean) ** 2 for x in args]) / n)


def ft_std(*args: int | float) -> float:
    """Compute the standard deviation arguments."""

    mean = sum(args) / len(args)
    n = len(args)

    return (sum([(x - mean) ** 2 for x in args]) / n) ** (1/2)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Apply statistics functions over a list of numbers."""

    func = {"mean": ft_mean, "median": ft_median, "quartile": ft_quartile,
            "std": ft_std, "var": ft_var}

    for v in kwargs.values():
        try:
            print(f"{v} : {func[v](*args)}") if v in func.keys() else ""
        except Exception:
            print("ERROR")
