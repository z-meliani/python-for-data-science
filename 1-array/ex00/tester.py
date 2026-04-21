from give_bmi import give_bmi, apply_limit

print("# Subject tests\n")

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


print("\n# My tests with error\n")

heights = [
            [0, "truc", None],
            [1.64, 2.14, 1.77],
            [1.64, 2.14, 1.77]
        ]

weights = [
            [65.3, 38.4, 44],
            [-1, "machin", None],
            [65.3, 38.4, 44]
        ]

limits = [26,
          17,
          "bidule"]

for h, w, l in zip(heights, weights, limits):
    bmi = give_bmi(h, w)
    print("bmi: ", bmi, type(bmi))
    print("limit: ", apply_limit(bmi, l))
    print()
