from ft_filter import ft_filter
import sys


def check_argv() -> list:
    """
    Ensure that two argument are provided and are valids.
    Return the list of words.
    """

    argc = len(sys.argv)

    try:
        assert argc == 3
        int(sys.argv[2])

        lst_s = [s.isalpha() for s in sys.argv[1].split()]
        for s in lst_s:
            assert s
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    return sys.argv[1].split()


def main():

    words = check_argv()

    n = int(sys.argv[2])

    filtered = ft_filter(lambda word: word if len(word) > n else None, words)

    print(list(filtered))


if __name__ == "__main__":
    main()
