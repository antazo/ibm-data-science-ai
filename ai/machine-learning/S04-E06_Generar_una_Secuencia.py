#!/usr/bin/env python3
# Section 4, Coding Exercise 6
# Generar una Secuencia de Números

import numpy as np

def generar_secuencia_numerica(minimo, maximo, paso):
    """
    Genera una secuencia de números enteros entre un valor mínimo y máximo con un paso dado.

    Parameters:
    minimo (int): Valor mínimo.
    maximo (int): Valor máximo.
    paso (int): Paso entre los números.

    Returns:
    list: Una secuencia de números enteros.
    """
    return np.arange(minimo, maximo, paso)

# Ejemplo de uso
minimo = 0
maximo = 10
paso = 2
resultado = generar_secuencia_numerica(minimo, maximo, paso)
print(resultado)

# Resultado esperado:
# [0 2 4 6 8]