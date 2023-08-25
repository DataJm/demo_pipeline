import pandas as pd
from sklearn.linear_model import LogisticRegression

def genera_modelo(df):
    X = df.drop(columns='survived')
    y = df['survived']
    modelo = LogisticRegression()
    modelo.fit(X,y)
    return modelo