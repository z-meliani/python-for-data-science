from array2D import slice_me

print("# Subject tests\n")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


print("\n# My tests with error\n")

# 1D array
simple = [1.80, 78.4]
print(slice_me(simple, 0, 5))


# Slicing error
print(slice_me(family, "truc", 5))
print(slice_me(family, -1, 1.3))
