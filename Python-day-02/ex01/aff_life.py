import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def aff_life(dt: pd.DataFrame):
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"
        ds = pd.DataFrame(dt)
        ds.loc['1800'].plot()
        plt.title('Morocco Life expectancy Projections')
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    # except Exception as err:
    #     print(f"ExceptionError: {err}")


def main():
    path = "life_expectancy_years.csv"
    dt = load(path)
    aff_life(dt)
    # try:
    #     path = "life_expectancy_years.csv"
    #     dt = load(path)
    #     aff_life(dt)
    # except Exception as err:
    #     print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
