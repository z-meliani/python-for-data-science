import matplotlib.pyplot as plt
from pathlib import Path
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

data_path = Path(__file__).resolve().parent.parent / "data"

array = ft_load(data_path / "landscape.jpg")
print(array)

funcs = {
    "original": lambda x: x,
    "ft_invert": ft_invert,
    "ft_red": ft_red,
    "ft_green": ft_green,
    "ft_blue": ft_blue,
    "ft_grey": ft_grey,
}

fig, axes = plt.subplots(3, 2, figsize=(10, 10))

for ax, (name, func) in zip(axes.flat, funcs.items()):
    img = func(array)

    ax.imshow(img)
    ax.set_title(name)
    ax.tick_params(labelbottom=False, labelleft=False)

plt.tight_layout()
plt.show()

print(ft_invert.__doc__)
