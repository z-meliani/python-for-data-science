import sys


def check_argv(argv: str) -> int:
    """
    Ensure that at most one argument is provided and return the argument count.
    """

    argc = len(sys.argv)

    try:
        assert argc <= 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    return argc


def get_string(argc: int) -> str:
    """
        Get a string passed as an argument.
        I no one is provided, prompt for one in stdin.
    """

    if argc == 1:
        print("What is the text to count?")
        return sys.stdin.readline()

    return sys.argv[1]


def count_char(string: str) -> dict:
    """
    Count the number of upper letters, lower letters, spaces,
    punctuation marks (.,;:!?), and digits in a string.
    Return a dictionary with the number element for each type.
    """

    count = {"upper": 0, "lower": 0, "mark": 0, "space": 0, "digit": 0}

    for char in string:
        match char:
            case ch if ch.isupper():
                count["upper"] += 1
            case ch if ch.islower():
                count["lower"] += 1
            case '.' | ',' | ';' | ':' | '!' | '?':
                count["mark"] += 1
            case ch if ch.isspace():
                count["space"] += 1
            case ch if ch.isdigit():
                count["digit"] += 1

    return count


def print_summary(func):
    """Wrap the function count_char to print a formatted summary."""
    def wrapper(text: str) -> dict:
        counts = func(text)
        total = sum(counts.values())
        print(f"The text contains {total} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['mark']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")
        return counts
    return wrapper


def main():

    argc = check_argv(sys.argv)

    string = get_string(argc)
    print() if string and (string[-1] != "\n") else ""

    print_summary(count_char)(string)

    return 0


if __name__ == "__main__":
    main()
