#!/usr/bin/env python3
# Section 10, Coding Exercise 10
# Regresión Lineal con Datos de Ventas

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Función de regresión lineal
def regresion_ventas(datos):
    # Crear un modelo de regresión lineal
    modelo = LinearRegression()

    # Ajustar el modelo a los datos
    modelo.fit(datos[['TV', 'Radio', 'Periodico']], datos['Ventas'])

    return modelo

# Ejemplo de uso con datos reales
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8],
    'Periodico': [69.2, 45.1, 69.3, 58.5, 58.4],
    'Ventas': [22.1, 10.4, 9.3, 18.5, 12.9]
}
df = pd.DataFrame(data)
modelo_regresion = regresion_ventas(df)

# Estimaciones de ventas para nuevos datos de inversión en publicidad
nuevos_datos = pd.DataFrame({'TV': [200, 60, 30], 'Radio': [40, 20, 10], 'Periodico': [50, 10, 5]})
estimaciones_ventas = modelo_regresion.predict(nuevos_datos)

print("Estimaciones de Ventas:")
print(estimaciones_ventas)

# Resultado esperado:
# Estimaciones de Ventas:
# [21.54261464  8.48121675  4.16961329]