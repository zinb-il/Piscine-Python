import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def aff_life(dt: pd.DataFrame, country: str = 'Morocco'):
    """this functiond plot the life expectancy for the specified country.

    Args:
        dt (pd.DataFrame): data frame to plot
        country (str, optional): The country to filter and plot data for.\
Defaults to 'Morocco'.
    """
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"

        assert isinstance(country, str), "The name of the country should a str"
        assert country in dt['country'].values, "This country \
doesn't existe in the file"
        # Methode 1
        years = dt.columns[1:].values
        life = dt[dt['country'] == country].iloc[0, 1:].values
        plt.plot(years, life)
        plt.xticks(range(0, len(years), 40), years[::40])
        ############################
        # Methode 2
        # ds = pd.DataFrame(dt.T)
        # ds.columns = ds.iloc[0]
        # ds = ds[1:]
        # ds[country].plot()
        # plt.xticks(range(0, len(ds.index), 40), ds.index[::40])
        ############################
        plt.title(f'{country.capitalize()} Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
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
