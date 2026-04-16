import sys

try:
    if len(sys.argv) == 1:
        sys.exit(0)
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.\n")
    else:
        print("I'm odd.\n")
except AssertionError as e:
    print(f"AssertionError: {e}\n")
    sys.exit(1)
except ValueError:
    print("AssertionError: argument is not an integer\n")
    sys.exit(1)
