#!/usr/bin/env python3
# Section 11, Coding Exercise 11
# Clasificación Binaria

import pandas as pd
from sklearn.linear_model import LogisticRegression

# Función de regresión logística
def regresion_logistica(datos):
    # Crear un modelo de regresión logística
    modelo = LogisticRegression()

    # Ajustar el modelo a los datos
    modelo.fit(datos[['Edad', 'Colesterol']], datos['Enfermedad'])

    return modelo

# Ejemplo de uso con datos de pacientes
data = {
    'Edad': [50, 35, 65, 28, 60],
    'Colesterol': [180, 150, 210, 130, 190],
    'Enfermedad': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
modelo_regresion_logistica = regresion_logistica(df)

# Estimaciones de clasificación binaria para nuevos datos
nuevos_datos = pd.DataFrame({'Edad': [45, 55], 'Colesterol': [170, 200]})
estimaciones_clasificacion = modelo_regresion_logistica.predict(nuevos_datos)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)

# Resultados esperados:
# Estimaciones de Clasificación:
# [1 1]