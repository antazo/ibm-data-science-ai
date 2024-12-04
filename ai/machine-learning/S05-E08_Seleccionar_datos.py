#!/usr/bin/env python3
# Section 5, Coding Exercise 8
# Seleccionar datos

import pandas as pd

def seleccionar_datos(dataframe, criterio):
    resultado = dataframe.query(criterio)
    return resultado

# Ejemplo de uso
data = {
    'nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'edad': [20, 22, 18, 25],
    'calificaciones': [90, 88, 75, 95]
}
 
df = pd.DataFrame(data)
criterio = 'edad > 18'
resultado = seleccionar_datos(df, criterio)
print(resultado)

# Resultado esperado:
#   nombre  edad  calificaciones
# 0  Alice    20              90
# 1    Bob    22              88
# 3  David    25              95