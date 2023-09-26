"""
This module takes a csv and returns statistics about it
"""
import matplotlib.pyplot as plt
import polars as pl


def descriptive_statistics(data):
    """
    Calculate descriptive statistics for a DataFrame.

    Parameters:
    data (pl.DataFrame): The input Polars DataFrame,
    which must contain numeric data.

    Returns:
    pl.DataFrame: A DataFrame containing descriptive statistics.
    """
    return data.describe()


def generating_plot(data, x_variable, y_variable, title, size=None):
    """
    Parameters:
        data: Polar DataFrame
        x_variable: String of the variable in axis X from data
        y_variable: String of the variable in axis Y from data
        size: String if a variable is required to
        title: String for the plot title
    """
    if size is None:
        area = 1
    else:
        area = data[size] * 10 / data[size].mean()
    # Labeling
    plt.scatter(data[x_variable], data[y_variable], s=area, alpha=0.5)
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.title(title)
    plt.show()
    plt.savefig(title + ".png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    data_pl = pl.read_csv("pythonproject/src/data/median-income-by-country-2023.csv")

    print(type(data_pl))

    print(type(descriptive_statistics(data_pl)))

    generating_plot(
        data_pl,
        x_variable="gdpPerCapitaPPP",
        y_variable="meanIncome",
        size="pop2023",
        title="GDP per Capita vs Avg income (size proportional Population)",
    )
