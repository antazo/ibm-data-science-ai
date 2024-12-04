#!/usr/bin/env python3
# Section 3, Coding Exercise 4
# Aplicar una Función y Filtrar Elementos en una Lista

def aplicar_funcion_y_filtrar(lista, valor_umbral):
    """
    Aplica una función a cada elemento de la lista y filtra los elementos
    que son mayores que un valor umbral.

    :param lista: Lista de números
    :param valor_umbral: Valor umbral
    :return: Lista de elementos que son mayores que el valor umbral
    """
    # Aplicar la función a cada elemento de la lista
    lista_resultado = [x ** 2 for x in lista]

    # Filtrar los elementos que son mayores que el valor umbral
    lista_filtrada = [x for x in lista_resultado if x > valor_umbral]

    return lista_filtrada

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
valor_umbral = 3
resultado = aplicar_funcion_y_filtrar(numeros, valor_umbral)
print(resultado)

# Resultado:
# [4, 9, 16, 25]