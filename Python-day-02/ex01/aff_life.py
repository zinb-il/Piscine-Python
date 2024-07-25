import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def aff_life(dt: pd.DataFrame, country: str = 'Morocco'):
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"
        assert isinstance(country, str), "The name of the country should a str"
        ds = pd.DataFrame(dt.T)
        ds.columns = ds.iloc[0]
        ds = ds[1:]
        assert country in ds.columns, "This country doesn't existe in the file" 
        ds[country].plot()
        plt.title(f'{country.capitalize()} Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.xticks(range(0, len(ds.index), 40), ds.index[::40])
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def main():
    try:
        path = "life_expectancy_years.csv"
        dt = load(path)
        aff_life(dt, 'Morocco')
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
