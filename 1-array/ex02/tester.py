from pathlib import Path

from load_image import ft_load

data_path = Path(__file__).resolve().parent.parent / "data"

print(ft_load(data_path / "landscape.jpg"))

print("\n---------\n")

print(ft_load(data_path / "animal.jpeg"))

print("\n---------\n")

print(ft_load("trucbidule.jpg"))
