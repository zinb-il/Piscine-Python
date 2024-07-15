from load_csv import load

def main():
    try:
        print(load("life_expectancy_years.csv"))
        load("test.csv")
        load("teeeeees.csv")
        load(None)
        load(['ree'])
        print(load.__doc__)
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
