[![Test workflow for Python template](https://github.com/nogibjj/rd278-w3-polars/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/nogibjj/rd278-w3-polars/actions/workflows/pythonapp.yml)

# Descriptive Statistics 

## Goals:
The template created in week one was updatedfor this assignment, particularly pandas was added to have descriptive statistics.

## Functions implemented

Data is loaded using **polars.read_csv**, and the function **dataframe.describe()** is used in module **source_code.py** to return the mean, min, percentiles and max.

## Test:
Besides linting and formating, the code had two test:
1. Checks if the file path is a csv file
2. Checks if the output is a polar DataFrame

# A Scatter plot

Just for the sake of ilustration, a plot was added to see the relationship between the GDP per Capita and the Average income, the data is for Countries and the size of each circle is proportional to the population of each country.

![Scatter Plot](https://github.com/nogibjj/rd278-w3-polars/blob/main/GDP%20per%20Capita%20vs%20Avg%20income%20(size%20proportional%20Population).png)
