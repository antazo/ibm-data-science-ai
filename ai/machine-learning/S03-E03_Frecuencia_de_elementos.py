#!/usr/bin/env python3
# Section 3, Coding Exercise 3
# Frecuencia de elementos en una lista

def contar_frecuencia(lista):
    """
    Cuenta la frecuencia de cada elemento en una lista.

    Parameters:
    lista (list): La lista de elementos.

    Returns:
    dict: Un diccionario donde las claves son los elementos de la lista y los valores son las frecuencias de esos elementos.
    """
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia

# Ejemplo de uso
elementos = [1, 2, 2, 3, 1, 2, 4, 5, 4]
resultado = contar_frecuencia(elementos)
print(resultado)

# Resultado esperado:
# {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}