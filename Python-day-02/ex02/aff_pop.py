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
        # years = dt.columns[1:].astype(int)
        # years = years[years <= 2050]
        # cc1 = dt[dt['country'] == c1].iloc[0,1:][years.astype(str)].values
        # cc1 = [conv(i) for i in cc1]
        # plt.plot(years, cc1, color = 'b', label = c1)
        # cc2 = dt[dt['country'] == c2].iloc[0,1:][years.astype(str)].values
        # cc2 = [conv(i) for i in cc2]
        # cc = np.concatenate((cc1,cc2))
        # plt.plot(years, cc2, color = 'g', label = c2)
        # plt.title('Population Projections')
        # plt.xlabel('Year')
        # plt.ylabel('Population')
        # plt.xticks(range(0, len(years), 40), years[::40])
        # plt.yticks(range(0, len(cc), 20), cc[::20])
        # plt.legend(loc = 'lower right')
        # plt.show()
        start_year = 1800
        end_year = 2050
        start_index = years.index(str(start_year))
        end_index = years.index(str(end_year)) + 1

        years_filtered = years[start_index:end_index]
        pop1 = data[country1][start_index:end_index]
        pop2 = data[country2][start_index:end_index]

        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(years_filtered, pop1, label=country1)
        plt.plot(years_filtered, pop2, label=country2)

        plt.title(f'Population Comparison: {country1} vs {country2}')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Add grid for better readability
        plt.grid(True, linestyle='--', alpha=0.7)

        # Adjust layout to prevent cutting off labels
        plt.tight_layout()

        # Show the plot
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
