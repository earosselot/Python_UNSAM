# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:39:01 2021

@author: Eduardo
"""

# %% 6.14
# Busqueda binaria


# def donde_insertar(lista, x, verbose=False):
#     '''Búsqueda binaria
#     Precondición: la lista está ordenada
#     Devuelve -1 si x no está en lista;
#     Devuelve p tal que lista[p] == x, si x está en lista
#     '''
#     if verbose:
#         print('[DEBUG] izq |der |medio')
#     pos = -1  # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if verbose:
#             print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
#         pos = medio
#         if x <= lista[medio]:
#             der = medio - 1  # descarto mitad derecha
#         else:                # if lista[medio] < x:
#             izq = medio + 1  # descarto mitad izquierda
#     if lista[pos] < x:       # x es mayor al ultimo elemento
#         return izq
#     else:
#         return pos


# donde_insertar([0, 2, 4, 5, 6], 4)     # 2
# donde_insertar([1, 2, 4, 6, 7, 8], 0)  # 0
# donde_insertar([0, 2, 4, 6], 3)        # 2
# donde_insertar([0, 2, 4, 6], 4)        # 2


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


# insertar([0, 1, 2], 3)   # [0, 1, 2, 3]
# insertar([0, 1, 2], -1)  # [-1, 0, 1, 2]
# insertar([0, 1, 3], 2)   # [0, 1, 2, 3]
# insertar([0, 1, 3], 1)   # 1
# insertar([0, 1, 3, 5, 6, 7], 2)  # [0, 1, 2, 3, 5, 6, 7]
# insertar([0, 1, 3, 5, 6, 7], 3)  # 3


# %% Ejercicio 6.17
# Complejidad de incrementar()


def incrementar(s):
    """
    Calcula la secuencia siguiente de una secuencia dada.
    Secuencia es una lista de 0's y 1's interpretada en binario
    """
    # s = secuencia.copy()
    carry = 1
    largo = len(s)
    for i in range(largo-1, -1, -1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


# Me parece que la complejidad de incrementar() es lineal. Recorre la lista 1
# vez


# %% Ejercicio 6.18
# Un ejemplo mas complejo


def listar_secuencias(n) -> list:
    """
    Devuelve una lista con todas las secuencias binarias de longuitud n
    """
    secuencia = [0] * n
    lista_secuencias = []
    lista_secuencias.append(secuencia)
    while 0 in secuencia:
        secuencia = incrementar(lista_secuencias[-1].copy())
        lista_secuencias.append(secuencia)
    return lista_secuencias


listar_secuencias(20)

# len | veces
# 1     1
# 2     4
# 3     8
# 5     32/
# n     2**n
# n+1   2**(n+1)

# listar_secuencias es exponencial en n. O(2**n)
