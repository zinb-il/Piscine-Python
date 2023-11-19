import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s, n = str(sys.argv[1]), int(sys.argv[2])
        arr = [i for i in ft_filter(lambda i: len(i) > n, s.split())]
        print(arr)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except (AssertionError, Exception) as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
