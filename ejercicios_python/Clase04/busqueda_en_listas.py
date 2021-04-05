# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:12:26 2021

@author: Eduardo
"""

def buscar_u_elemento(lista, elemento):
    """ Función que recibe un lista y un elemento y devuelve la posición de la
    última aparición de ese elemento en la lista, o -1 si el elemento no
    está en la lista.
    """
    pos = len(lista) - 1  
    while pos >= 0:
        if lista[pos] == elemento:
            break
        pos -= 1
    return pos


def buscar_n_elemento(lista, elemento):
    """ Función que recibe un lista y un elemento y devuelve la cantidad de 
    veces que aparece el elemento e en la lista.
    """
    numElem = 0
    for listElem in lista:
        if listElem == elemento:
            numElem += 1
    return numElem


def maximo(lista):
    """ Busca el maximo valor de una lista de numeros positivos
    """
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    maxVal = lista[0] # Lo inicializo en 0
    for listElem in lista: # Recorro la lista y voy guardando el mayor
        if listElem > maxVal:
            maxVal = listElem
    return maxVal

maximo([1,2,7,2,3,4])   # 7
maximo([-5,4])          # 4
maximo([-5,-4])         # -4


def minimo(lista):
    """ Busca el minimo valor de una lista de numeros positivos
    """
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    minVal = lista[0] # Lo inicializo en 0
    for listElem in lista: # Recorro la lista y voy guardando el mayor
        if listElem < minVal:
            minVal = listElem
    return minVal

minimo([-5,-4])         # -5
minimo([1,2,7,2,3,4])   # 1
