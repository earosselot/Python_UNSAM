# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:56:18 2021

@author: Eduardo
"""
# %% Ejercicio 4.18
#   Lectura de todos los arboles

import csv
import random


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

# %% Ejercicio 5.24
# Histograma altos Jacarandás


import matplotlib.pyplot as plt
import numpy as np


# Extracto 4.19 -Lista de altos de Jacarandá
alturas = [float(arbol['altura_tot']) for arbol in arboleda]
alturasJacaranda = [float(arbol['altura_tot']) for arbol in arboleda
                    if arbol['nombre_com'] == 'Jacarandá']


def histograma_altura_arboles(alturasEspecie):
    """
    Función que recibe una lista de alturas de una especie y genera un
    histograma.
    """
    plt.figure()
    plt.hist(alturasEspecie, bins=50)
    plt.xlabel('altura(m)')
    plt.ylabel('cantidad(n)')


histograma_altura_arboles(alturasJacaranda)

# %% Ejercicio 5.25
# Scatterplot

# Ejercicio 4.20 - Lista de altos y diámetros de Jacarandá
AltoDiamJacaranda = [(int(arbol['altura_tot']), int(arbol['diametro']))
                     for arbol in arboleda
                     if arbol['nombre_com'] == 'Jacarandá']


def scatter_alto_diam(AltoDiamEspecie, especie):
    """
    Función que recibe una lista de tuplas con formato (alto, diametro) de una
    especie y devuelve un grafico scatter de altura vs diametro en un color
    aleatorio.
    """
    vector_alturas_diam = np.array(AltoDiamEspecie)
    d = vector_alturas_diam[:, 0]
    h = vector_alturas_diam[:, 1]
    color = tuple([random.random() for i in range(3)])
    plt.scatter(d, h, c=color, alpha=0.05)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f'Relación diámetro-alto para {especie}')


plt.figure()
scatter_alto_diam(AltoDiamJacaranda, 'Jacarandás')

# %% Ejercicio 5.26
# Scatterplot para diferentes especies


import os
import matplotlib.pyplot as plt
import numpy as np
import random


nombre_archivo = os.path.join('..', 'Data', 'arbolado.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dicc_medidas = medidas_de_especies(especies, arboleda)


def muchos_scatters(medidas):
    """
    Función que recibe un diccionario de formato:
    {especie: [(alto, diam), ( , ), ...]}
    y plotea un grafico scatter de alto vs diametro para cada especie.
    """
    for especie in medidas:
        plt.figure()
        scatter_alto_diam(medidas[especie], especie)


muchos_scatters(dicc_medidas)


def un_scatter(medidas):
    """
    Función que recibe un diccionario de formato:
    {especie: [(alto, diam), ( , ), ...]}
    y plotea un grafico scatter de alto vs diametro donde se muestran todas
    las especies en distintos colores.
    """
    plt.figure()
    for especie in medidas:
        scatter_alto_diam(medidas[especie], especie)


un_scatter(dicc_medidas)
