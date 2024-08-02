import numpy as np
import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def conv(v: str) -> float:
    """Convert a string with suffix 'M' or 'K' to a float \
representing the actual number.

    Args:
        v (str): The string to convert. It may contain 'M' \
for millions or 'K' for thousands.

    Returns:
        float: the converted value
    """
    if 'M' in v:
        return float(v.replace('M', '')) * 1000000
    elif 'K' in v:
        return float(v.replace('K', '')) * 1000
    else:
        return float(v)


def aff_pop(dt: pd.DataFrame, c1: str = 'France', c2: str = 'Belgium'):
    """this function plot the population for the specified countries \
vs other countries.

    Args:
        dt (pd.DataFrame): data frame
        c1 (str, optional): The country to filter and plot data for. \
Defaults to 'France'.
        c2 (str, optional): The country to filter and plot data for. \
Defaults to 'Belgium'.
    """
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"
        assert isinstance(c1, str) and isinstance(c2, str), "The \
name of the country should a str"
        convert = np.vectorize(conv)
        years = dt.columns[1:].astype(int)
        years = years[years <= 2050]
        cc1 = dt[dt['country'] == c1].iloc[0, 1:][years.astype(str)].values
        cc1 = convert(cc1)
        cc2 = dt[dt['country'] == c2].iloc[0, 1:][years.astype(str)].values
        cc2 = convert(cc2)
        cc = np.sort(np.concatenate((cc1, cc2)))
        ticks = np.arange(20000000, int(max(cc)), 20000000)
        labels = [f'{int(tick / 1e6)}M' for tick in ticks]
        plt.plot(years, cc1, color='b', label=c1)
        plt.plot(years, cc2, color='g', label=c2)
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(range(min(years), max(years), 40), years[::40])
        plt.yticks(ticks, labels)
        plt.legend(loc='lower right')
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def main():
    try:
        path = 'population_total.csv'
        data = load(path)
        aff_pop(data, 'Belgium', 'France')
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
