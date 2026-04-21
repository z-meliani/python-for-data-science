import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image.
    Return a 3D array.
    """

    try:
        img = Image.open(path)
        img = np.array(img)

        print(f"The shape of image is: {img.shape}")

    except Exception as e:
        print(f"Error: {e}")
        return None

    return img
