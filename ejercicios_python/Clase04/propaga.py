# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:34:38 2021

@author: Eduardo
"""

def propagar(lista):
    """
    recibe una lista con 0's, 1's y -1's y devuelve una lista donde los 1's 
    se propagan a sus vecinos con 0.
    """
    n = len(lista)
    i = 0
    
    # propaga a derecha
    while i < n-1:
        if lista[i] == 1 and lista[i+1] == 0:
            lista[i+1] = 1
        i += 1
    
    # propaga a izquierda. En este momento i = len(lista) - 1
    while i > 0:
        if lista[i] == 1 and lista[i-1] == 0:
            lista[i-1] = 1
        i -= 1
        
    return lista

propagar([ 0, 0, 0, 1, 0, 0]) 
# [1, 1, 1, 1, 1, 1]

propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]