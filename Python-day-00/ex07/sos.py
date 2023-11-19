import sys


def main():
    try:
        s = []
        errmsg = "the arguments are bad"
        NESTED_MORSE = {" ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. "}
        assert len(sys.argv) == 2, errmsg
        s = str(sys.argv[1]).upper().strip()
        for i in s:
            assert i in NESTED_MORSE.keys(), errmsg
        s = "".join([NESTED_MORSE.get(j) for j in s]).strip()
        print(s)
    except (AssertionError, ValueError):
        print(f"AssertionError: {errmsg}")
    except Exception as err:
        print(f"ExceptionErr: {err}")


if __name__ == "__main__":
    main()
