import sys


def check_argv() -> str:
    """
    Ensure that one argument is provided.
    The argument should be a string of alphanumeric characters.
    Return a string in upper case.
    """

    argc = len(sys.argv)

    try:
        assert argc == 2

        for char in sys.argv[1]:
            assert char.isalnum() or char == " "
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    return sys.argv[1].upper()


def convert_alnum_to_morse(c) -> str:
    """
    Convert an alphanumeric character to its Morse code.
    Return a string.
    """

    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    return NESTED_MORSE.get(c, None)


def convert_string_to_morse(string) -> list:
    """
    Convert a string to its Morse code.
    Return a list.
    """

    morse = []

    for c in string:
        try:
            c = convert_alnum_to_morse(c)
            assert c
        except AssertionError:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        morse.append(c)

    return morse


def main():

    string = check_argv()

    print(f"{' '.join(convert_string_to_morse(string))}")

    return 0


if __name__ == "__main__":
    main()
