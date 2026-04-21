import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Return a 2D array with elements between start and end (not included) index.
    """
    try:
        res = np.array(family)
        if len(res.shape) != 2:
            raise TypeError("argument is not a 2D array")
        print(f"My shape is : {res.shape}")

        res = res[start:end]
        print(f"My new shape is : {res.shape}")

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res.tolist()
