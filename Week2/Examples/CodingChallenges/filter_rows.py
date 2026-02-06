import pandas as pd

def filter_rows(dataframe: pd.DataFrame, col, func):
    return dataframe[~dataframe[col].apply(func)]

#https://www.codewars.com/kata/5ea2baed9345eb001e8ce394