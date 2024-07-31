import pandas as pd
import numpy as np
from load_csv import load
from matplotlib import pyplot as plt


def conv(v: str) -> float:
    if 'M' in v:
        return float(v.replace('M', '')) * 1000000
    elif 'K' in v:
        return float(v.replace('K', '')) * 1000
    else:
        return float(v)


def aff_pop(dt: pd.DataFrame, c1: str = 'France', c2: str = 'Belgium'):
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"
        assert isinstance(c1, str) and isinstance(c2, str), "The \
name of the country should a str"
        convert = np.vectorize(conv)
        years = dt.columns[1:].astype(int)
        years = years[years <= 2050]
        cc1 = dt[dt['country'] == c1].iloc[0,1:][years.astype(str)].values
        cc1 = convert(cc1)
        cc2 = dt[dt['country'] == c2].iloc[0,1:][years.astype(str)].values
        cc2 = convert(cc2)
        cc = np.sort(np.concatenate((cc1,cc2)))
        plt.plot(years, cc1, color = 'b', label = c1)
        plt.plot(years, cc2, color = 'g', label = c2)
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(range(min(years), max(years), 40), years[::40])
        plt.yticks(range(int(min(cc)), int(max(cc)), 20000000))
        plt.legend(loc = 'lower right')
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
