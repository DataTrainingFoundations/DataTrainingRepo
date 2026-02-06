import pandas as pd

def rename_columns(df: pd.DataFrame, names):
    new_df = df.copy()
    new_df.columns = names
    return new_df

#https://www.codewars.com/kata/5e60cdcd01712200335bd676