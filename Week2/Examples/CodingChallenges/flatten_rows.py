#https://www.codewars.com/kata/615bf5f446a1190007bfb9d9
import pandas as pd

def flatten_rows(dataframe: pd.DataFrame, col):
    return dataframe.copy().explode(col, ignore_index=True)