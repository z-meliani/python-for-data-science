import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Compute BMI from height and weight lists."""

    try:
        h = np.asarray(height, dtype=float)
        w = np.asarray(weight, dtype=float)

        if h.shape != w.shape:
            raise ValueError("height and weight must have same size")

        if np.any(h == 0):
            raise ZeroDivisionError("height contains zero")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None

    bmi = (w / (h**2)).round(2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if BMI values are above a limit."""

    try:
        result = [x > limit for x in bmi]
    except Exception as e:
        print(f"Error: {e}")
        return None

    return result
