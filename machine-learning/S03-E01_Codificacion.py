#!/usr/bin/env python3
# Section 3, Coding Exercise 1
# Ejercicio de codificación : Operaciones Matemáticas

def operaciones_matematicas(a, b):
    """
    Realiza operaciones matemáticas básicas entre dos números.

    Parameters:
    a (float): El primer número.
    b (float): El segundo número.

    Returns:
    tuple: Una tupla que contiene los resultados de la suma, resta, multiplicación, división y residuo.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None  # Evitar la división por cero
    residuo = a % b if b != 0 else None   # Evitar el residuo por cero
    return suma, resta, multiplicacion, division, residuo


# Ejemplo de uso
a = 10
b = 3

resultado = operaciones_matematicas(a, b)

print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])
print("Residuo:", resultado[4])

# Resultado esperado:
# Suma: 13
# Resta: 7
# Multiplicación: 30
# División: 3.3333333333333335
# Residuo: 1