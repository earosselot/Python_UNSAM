# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:56:18 2021

@author: Eduardo
"""
# %% Ejercicio 4.18
#   LEctura de todos los arboles

import csv


def leer_arboles(nombre_archivo):
    """
    Lee el archivo indicado y devuelve una lista de diccionarios con la
    informacion de los arboles en el archivo. Cada diccionario representa un
    arbol.
    """
    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    arboleda = [dict(zip(headers, arbol)) for arbol in rows]

    return arboleda


arboleda = leer_arboles('../Data/arbolado.csv')
arboleda_chica = leer_arboles('../Data/arbolado_prueba.csv')


# %% Ejercicio 4.19
# Lista de altos de Jacarandá

alturas = [float(arbol['altura_tot']) for arbol in arboleda]
alturasJacaranda = [float(arbol['altura_tot']) for arbol in arboleda
                    if arbol['nombre_com'] == 'Jacarandá']

# %% Ejercicio 4.20
# Lista de altos y diámetros de Jacarandá

AltoDiamJacaranda = [(int(arbol['altura_tot']), int(arbol['diametro']))
                     for arbol in arboleda
                     if arbol['nombre_com'] == 'Jacarandá']


# %% Ejercicio 4.21
# Diccionario con medidas

def medidas_de_especies(especies, arboleda):
    """
    Recibe una lista de nombres de especies y la arboleda y devuelve un
    diccionario donde las claves son las especies y los valores son listas
    de tuplas (altura, diametro) para todos los ejemplares de esa especie.
    """

    diccionario = {especie: [(int(arbol['altura_tot']), int(arbol['diametro']))
                             for arbol in arboleda
                             if arbol['nombre_com'] == especie]
                   for especie in especies}
    return diccionario


especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
