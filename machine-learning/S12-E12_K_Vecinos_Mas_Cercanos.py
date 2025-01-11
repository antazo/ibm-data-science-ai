#!/usr/bin/env python3
# Section 12, Coding Exercise 12
# K Vecinos Más Cercanos para Clasificación

csv_file = "machine-learning/dataset/iris.csv"  # archivo de datos

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Función de clasificación KNN
def knn_clasificacion(datos, k=3):
    # Separar las características y la variable objetivo
    X = datos.iloc[:, :-1]
    y = datos.iloc[:, -1]
    
    # Crear el modelo KNN
    modelo = KNeighborsClassifier(n_neighbors=k)
    
    # Ajustar el modelo a los datos
    modelo.fit(X, y)
    
    return modelo

# Ejemplo de uso con el conjunto de datos Iris
data = pd.read_csv(csv_file)
modelo_knn = knn_clasificacion(data, k=3)

# Estimaciones de clasificación para nuevas muestras
nuevas_muestras = pd.DataFrame({
    'LargoSepalo': [5.1, 6.0, 4.4],
    'AnchoSepalo': [3.5, 2.9, 3.2],
    'LargoPetalo': [1.4, 4.5, 1.3],
    'AnchoPetalo': [0.2, 1.5, 0.2]
})

estimaciones_clasificacion = modelo_knn.predict(nuevas_muestras)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)

# Resultados esperados:
# Estimaciones de Clasificación:
# ['setosa' 'versicolor' 'setosa']