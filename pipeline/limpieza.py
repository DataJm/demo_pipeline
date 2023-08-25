import pandas as pd

def generar_df_limpio(archivo):
    datos = pd.read_csv(archivo)
    datos = datos.drop(columns=['deck'])
    datos = datos[['survived','sex','age']]
    datos = datos.dropna()
    return datos