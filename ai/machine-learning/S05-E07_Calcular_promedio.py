#!/usr/bin/env python3
# Section 5, Coding Exercise 7
# Calcular promedio

import pandas as pd

def calcular_promedio(dataframe):
    """
    Calcula el promedio de cada columna en un DataFrame.

    Parameters:
    dataframe (pd.DataFrame): Un DataFrame de pandas.

    Returns:
    pd.Series: Una serie de pandas que contiene el promedio de cada columna.
    """
    return dataframe.mean()

# Ejemplo de uso
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
 
df = pd.DataFrame(data)
resultado = calcular_promedio(df)
print(resultado)

# Resultado esperado:
# A     2.5
# B     6.5
# C    10.5
# dtype: float64