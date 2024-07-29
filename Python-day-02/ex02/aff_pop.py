import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt



def aff_pop(dt: pd.DataFrame, c1: str = 'France', c2: str = 'Belgium'):
    try:
        assert isinstance(dt, pd.DataFrame), "The data should \
be pd.DataFrame type"
        assert isinstance(c1, str) and isinstance(c2, str), "The \
name of the country should a str"
        years = dt.columns[1:].astype(int)
        # cc1 = dt[dt['country'] == c1].iloc[0,1:].values
        # # cc2 = dt[dt['country'] == c2].iloc[0,1:].values
        # plt.plot(years, cc1, color = 'b', label = c1)
        # # plt.plot(years, cc2, color = 'g', label = c2)
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.xticks(range(1800, len(years), 40))
        plt.xlim(0,2050)
        # plt.ylabel('Population')
        # # plt.yticks(range(0, len(cc2), 20), cc2[::20])
        # plt.legend(loc = 'lower right')
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")

def main():
    try:
        path = 'population_total.csv'
        data = load(path)
        aff_pop(data, 'France', 'Belgium')
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")

if __name__ == "__main__":
    main()
