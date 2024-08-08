import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def projection_life(dt1: pd.DataFrame, dt2: pd.DataFrame, year: int = 1900):
    """This function displays the projection of life expectancy in relation \
to the gross national product of the year

    Args:
        dt1 (pd.DataFrame): life expectancy over the years
        dt2 (pd.DataFrame): income per person
        year (int, optional): year. Defaults to 1900.
    """
    assert isinstance(dt1, pd.DataFrame) and isinstance(dt1, pd.DataFrame), "\
The data should be pd.DataFrame type"
    assert isinstance(year, int) and year > 0, "The year \
sould be a positive integer"
    assert str(year) in dt1.columns and str(year) in dt2.columns, "\
This year doesn't exist in your data"
    df1 = dt1.copy().dropna()
    df2 = dt2.copy().dropna()
    d_indexs = dt1[~dt1.index.isin(df1.index)].index
    df2 = df2.drop(d_indexs)
    xaxis = df2[str(year)].values
    yaxis = df1[str(year)].values
    xticks = [300, 1000, 10000]
    labels = ['300', '1k', '10k']
    plt.plot(xaxis, yaxis, 'o')
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(xticks, labels)
    plt.show()


def main():
    try:
        path1 = "life_expectancy_years.csv"
        path2 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        df1 = load(path1)
        df2 = load(path2)
        projection_life(df1, df2, 1900)
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
