#!/usr/bin/env python3
# Section 4, Coding Exercise 5
# Generar N números aleatorios enteros entre un valor mínimo y máximo

import numpy as np

def generar_numeros_enteros_aleatorios(N, minimo, maximo):
    """
    Genera N números enteros aleatorios entre un valor mínimo y máximo.

    Parameters:
    N (int): Número de elementos a generar.
    minimo (int): Valor mínimo.
    maximo (int): Valor máximo.

    Returns:
    list: Una lista de N números enteros aleatorios.
    """
    return np.random.randint(minimo, maximo + 1, N)

# Ejemplo de uso
N = 5
minimo = 1
maximo = 10
resultado = generar_numeros_enteros_aleatorios(N, minimo, maximo)
print(resultado)

# Resultado esperado:
# [4, 10, 1, 8, 2]