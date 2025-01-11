#!/usr/bin/env python3
# Section 3, Coding Exercise 2
# Calcular la suma y promedio de una lista de números

def calcular_suma_y_promedio(lista_numeros):
    """
    Realiza operaciones matemáticas básicas entre dos números.

    Parameters:
    a (float): El primer número.
    b (float): El segundo número.

    Returns:
    tuple: Una tupla que contiene los resultados de la suma, resta, multiplicación, división y residuo.
    """
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros) if len(lista_numeros) > 0 else 0
    return {"suma": suma, "promedio": promedio}

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]

resultado = calcular_suma_y_promedio(numeros)

print("Suma:", resultado["suma"])
print("Promedio:", resultado["promedio"])

# Resultado esperado:
# Suma: 15
# Promedio: 3.0