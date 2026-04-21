import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from load_image import ft_load


def slice_image(image, start=(0, 0), end=(-1, -1), channel=None):
    """
    Take a 3D array.
    Return a sliced channel (2D array) of the original array between start and
    end.
    If channel is None return
    """

    try:
        img = np.array(image)
        if len(img.shape) != 3:
            raise TypeError("argument is not a 3D array")

        res = img[start[0]:end[0], start[1]:end[1], channel]

        print(f"New shape after slicing: {res.shape}\n{res}")

    except Exception as e:
        print(f"Error: {e}")
        return None

    return res


def main():

    data_path = Path(__file__).resolve().parent.parent / "data"

    animal = ft_load(data_path / "animal.jpg")
    print(animal)

    animal_slice = slice_image(animal, (200, 700), (750, 1250), 2)
    print(animal_slice)

    plt.imshow(animal_slice, cmap="grey")
    plt.show()

    return 0


if __name__ == "__main__":
    main()
