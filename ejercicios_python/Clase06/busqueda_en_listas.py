# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:12:26 2021

@author: Eduardo
"""

# %% Ejercicio 4.6
# Buesquedas de un elemento

# def buscar_u_elemento(lista, elemento):
#     """ Función que recibe un lista y un elemento y devuelve la posición de la
#     última aparición de ese elemento en la lista, o -1 si el elemento no
#     está en la lista.
#     """
#     pos = len(lista) - 1  
#     while pos >= 0:
#         if lista[pos] == elemento:
#             break
#         pos -= 1
#     return pos

# buscar_u_elemento([1,2,3,2,3,4],1)  # 0
# buscar_u_elemento([1,2,3,2,3,4],2)  # 3
# buscar_u_elemento([1,2,3,2,3,4],3)  # 4
# buscar_u_elemento([1,2,3,2,3,4],5)  # -1

# def buscar_n_elemento(lista, elemento):
#     """ Función que recibe un lista y un elemento y devuelve la cantidad de 
#     veces que aparece el elemento e en la lista.
#     """
#     numElem = 0
#     for listElem in lista:
#         if listElem == elemento:
#             numElem += 1
#     return numElem

# buscar_n_elemento([1, 1, 1, 3, 2, 1, 5, 3, 1, 5, -1, 2, 4], 1)  # 5
# buscar_n_elemento([1, 1, 1, 3, 2, 1, 5, 3, 1, 5, -1, 2, 4], 2)  # 2
# buscar_n_elemento([1, 1, 1, 3, 2, 1, 5, 3, 1, 5, -1, 2, 4], -1) # 1
# buscar_n_elemento([1, 1, 1, 3, 2, 1, 5, 3, 1, 5, -1, 2, 4], -2) # 0

# %%
# Ejercicio 4.7 Busqueda de maximo y minimo

# def maximo(lista):
#     """ Busca el maximo valor de una lista de numeros
#     """
#     # m guarda el máximo de los elementos a medida que recorro la lista. 
#     maxVal = lista[0] # Lo inicializo en 0
#     for listElem in lista: # Recorro la lista y voy guardando el mayor
#         if listElem > maxVal:
#             maxVal = listElem
#     return maxVal

# maximo([1,2,7,2,3,4])   # 7
# maximo([-5,4])          # 4
# maximo([-5,-4])         # -4


# def minimo(lista):
#     """ Busca el minimo valor de una lista de numeros
#     """
#     # m guarda el máximo de los elementos a medida que recorro la lista. 
#     minVal = lista[0] # Lo inicializo en 0
#     for listElem in lista: # Recorro la lista y voy guardando el mayor
#         if listElem < minVal:
#             minVal = listElem
#     return minVal

# minimo([-5,-4])         # -5
# minimo([1,2,7,2,3,4])   # 1


# %% Ejercicio 6.13
# Busqueda lineal sobre listas ordeandas


def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        print(i)
        if e < z:
            break
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

busqueda_lineal_lordenada([1,2,3,6,6,9], 4)

# En el peor caso hace la misma cantidad de operaciones que la busqueda anterior. O(n)
# Al parecer no es mas eficiente


