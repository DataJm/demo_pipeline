# Ejecuta todos los scripts
import pandas as pd
from sklearn.linear_model import LogisticRegression

from limpieza import generar_df_limpio
from generarDummies import genera
from modelo import genera_modelo

def main():
    archivo = "./dataset/titanic.csv"
    datos = generar_df_limpio(archivo)
    datos = genera(datos)
    modelo = genera_modelo(datos)

    # Hacer predicciones
    simulacion = pd.DataFrame({
        'age': [20,30],
        'sex_male': [1, 0]
    })

    print(modelo.predict(simulacion))

main()