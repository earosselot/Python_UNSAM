# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:32:58 2021

@author: Eduardo
"""

# %% Ejercicio 4.8
# Intertir una lista

def invertir_lista(lista):
    """ Devuelve una lista con sus elementos invertidos
    """
    
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0, e)
    return invertida

invertir_lista([1, 2, 3, 4, 5]) # [5, 4, 3, 2, 1]
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']

