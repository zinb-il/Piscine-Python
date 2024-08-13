from statistics import ft_statistics


def main():
    try:
        ft_statistics(1, 42, 360, 11, 64,
                      toto="mean", tutu="median", tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                      hello="std", world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                      ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
        print("-------------------------------------------------")
        ft_statistics(10, 20, 40, 50,
                      toto="mean", tutu="median", tata="quartile")
        print("-----")
        ft_statistics(10, 1, 8, 14, 10, 13, 10, 14, 1, tata="quartile")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
