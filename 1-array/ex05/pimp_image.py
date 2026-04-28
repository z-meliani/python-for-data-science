import numpy as np


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""

    try:
        res = np.array(array)

        res = 255 - res

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res


def ft_red(array) -> np.array:
    """Set the green and blue channel to 0."""

    try:
        res = np.array(array)

        res[:, :, 1:] *= 0

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res


def ft_green(array) -> np.array:
    """ Set the ed and blue channel values to 0."""

    try:
        res = np.array(array)

        res[:, :, 0] -= res[:, :, 0]
        res[:, :, 2] -= res[:, :, 2]

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res


def ft_blue(array) -> np.array:
    """ Set the red and green channel values to 0."""

    try:
        res = np.array(array)

        res[:, :, :2] = 0

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res


def ft_grey(array) -> np.array:
    """Convert an RGB image to grayscale and return it as an RGB image."""

    try:
        res = np.array(array, dtype=float)

        res = np.sum((res / 3), axis=2).astype(int)

        res = np.stack([res, res, res], axis=2)

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res
