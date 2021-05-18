# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:41:04 2021

@author: Eduardo
"""


def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if desde <= hasta:
        for i in range(desde, hasta + 1):
            suma += i
    return suma


def sumar_enteros_triangular(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma_desde = (desde - 1) * (desde) / 2
    suma_hasta = hasta * (hasta + 1) / 2
    return suma_hasta - suma_desde
