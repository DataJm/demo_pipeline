import pandas as pd

def genera(df):
    df_dummies = pd.get_dummies(df, drop_first=True)
    return df_dummies