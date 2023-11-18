import sys


def ft_count(s: str) -> any:
    '''cette fonction prend en argument une seule chaîne et
    affiche la somme de ses caractères majuscules, minuscules,
    ponctuation, chiffres et espaces. minuscules, des caractères
    de ponctuation, des chiffres et des espaces'''

    p ="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    print(f"The text contains {len(s)} characters:")
    print(f"{len([i for i in s if i.isupper()])} upper letters")
    print(f"{len([i for i in s if i.islower()])} lower letters")
    print(f"{len([i for i in s if i in p])} punctuation marks")
    print(f"{len([i for i in s if i.isspace()])} spaces")
    print(f"{len([i for i in s if i.isdigit()])} digits")


def main():
    try:
        s = ''
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            s = input("What is the text to count?\n")
        else:
            s = sys.argv[1]
        ft_count(s)
        print(ft_count.__doc__)
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
