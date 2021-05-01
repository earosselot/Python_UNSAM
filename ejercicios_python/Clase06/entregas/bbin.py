# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:19:31 2021

@author: Eduardo
"""

# %% 6.14
# Busqueda binaria


def donde_insertar(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        pos = medio
        if x <= lista[medio]:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    if lista[pos] < x:       # x es mayor al ultimo elemento
        return izq
    else:
        return pos


# %% Ejercicio 6.15
# Insertar un elemento en una lista

def insertar(lista: list, x) -> list:
    """
    Precondición: la lista esta ordenada y contiene solo un tipo de datos
    Devuelve la lista ordenada insertando el elemento x en su posición
    correspondiente y la posición, de manera que la lista sigue estando
    ordenada.
    Devuelve la posición de x si x está en la lista.
    """
    index = donde_insertar(lista, x, False)
    if len(lista) == index:
        return (lista + [x], index)
    elif lista[index] == x:
        return index
    else:
        return (lista[:index] + [x] + lista[index:], index)


print(insertar([0, 1, 2], 3))   # [0, 1, 2, 3]
print(insertar([0, 1, 2], -1))  # [-1, 0, 1, 2]
print(insertar([0, 1, 3], 2))   # [0, 1, 2, 3]
print(insertar([0, 1, 3], 1))   # 1
print(insertar([0, 1, 3, 5, 6, 7], 2))  # [0, 1, 2, 3, 5, 6, 7]
print(insertar([0, 1, 3, 5, 6, 7], 3))  # 3
