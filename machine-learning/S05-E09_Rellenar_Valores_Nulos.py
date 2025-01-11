#!/usr/bin/env python3
# Section , Coding Exercise 
# Rellenar Valores Nulos con la Media de una Columna

import pandas as pd

def rellenar_con_media(dataframe, columna):
    """
    Rellena los valores nulos de una columna con la media de dicha columna.
    """
    # Calcula la media de la columna
    media = dataframe[columna].mean()
    
    # Rellena los valores nulos con la media
    dataframe[columna].fillna(media, inplace=True)
    
    return dataframe

# Ejemplo de uso
data = {
    'nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'edad': [20, None, 18, 25, None],
    'calificaciones': [90, 88, None, None, 95]
}
 
df = pd.DataFrame(data)
columna = 'calificaciones'
 
resultado = rellenar_con_media(df, columna)
print(resultado)


# Resultado esperado:
#     nombre  edad  calificaciones
# 0    Alice  20.0            90.0
# 1      Bob   NaN            88.0
# 2  Charlie  18.0            91.0
# 3    David  25.0            91.0
# 4      Eve   NaN            95.0