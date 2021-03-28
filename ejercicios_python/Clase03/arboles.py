# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:45:13 2021

@author: Eduardo Rosselot
"""
#%% Ejercicio 3.18 
# Lectura de los árboles de un parque

import csv
from pprint import pprint

# def leer_parque(nombre_archivo, parque):
#     """
#     Abre un archivo de arboles y devuelve los arboles de un parque.
#     Devuelve una lista de diccionarios, donde cada diccionario representa un
#     arbol. Dentro de cada arbol, las claves son los headers del archivo y los
#     valores son los correspondientes a ese arbol.
#     """
#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         lista = []
#         for row in rows:
#             if row[10] == parque:
#                 lista.append(dict(zip(headers,row)))
#     return lista
                

# parque = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ')
# pprint(parque)

#%% Ejercicio 3.19
# Determinar las especies de un parque

def especies(lista_arboles):
    """
    Toma como entada una lista de arboles, donde cada arbol es un diccionario.
    Y devuelve una conjunto con las especies presentes en esa lista (sin 
    duplicar).
    """
    especies_raw = []
    for arbol in lista_arboles:
        especies_raw.append(arbol['nombre_com'])
    conjunto_especies = set(especies_raw)
    return conjunto_especies
    
# especies = especies(parque)
# pprint(especies)


#%% Ejercicio 3.20
# Contar ejemplares por especie

from collections import Counter

def contar_ejemplares(lista_arboles):
    """
    Devuelve un diccionario donde las claves son los arboles y el valor es la
    cantidad de cada arbol en la lista_arboles.
    """
    numero_ejemplares = Counter()
    for arbol in lista_arboles:
        numero_ejemplares[arbol['nombre_com']] += 1
    return numero_ejemplares

# parque = leer_parque('../Data/arbolado.csv', 'CENTENARIO')
# numero_ejemplares = contar_ejemplares(parque)
# pprint(numero_ejemplares.most_common(5))


#%% Ejercicio 3.21
# Alturas de una especie en una lista

import statistics

def leer_parque(nombre_archivo, parque):
    """
    Abre un archivo de arboles y devuelve los arboles de un parque.
    Devuelve una lista de diccionarios, donde cada diccionario representa un
    arbol. Dentro de cada arbol, las claves son los headers del archivo y los
    valores son los correspondientes a ese arbol.
    Los valores numéricos se convierten a int o a float segun corresponda.
    """
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        lista = []
        for row in rows:
            if row[10] == parque:
                for i, item in enumerate(row):
                    if item.isdigit():
                        row[i] = int(item)
                    elif item.replace('-', '').replace('.', '').isdigit():
                        row[i] = float(item)
                lista.append(dict(zip(headers,row)))
    return lista

def obtener_alturas(lista_arboles, especie):
    """
    Devuelve una lista con las alturas de los arboles de la especie dentro de 
    la lista_arboles.
    """
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(arbol['altura_tot'])
    return alturas


# parque = leer_parque('../Data/arbolado.csv', 'CENTENARIO') 
# alturas = obtener_alturas(parque, 'Jacarandá')
# print(max(alturas))
# print(statistics.mean(alturas))
# print(alturas)

#%% Ejercicio 3.22
# Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    """
    Devuelve una lista con las inclinaciones de los arboles de la especie dentro de 
    la lista_arboles.
    """
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(arbol['inclinacio'])
    return inclinaciones
    
# parque = leer_parque('../Data/arbolado.csv', 'CENTENARIO') 
# inclinaciones = obtener_alturas(parque, 'Jacarandá')
# print(max(inclinaciones))
# print(statistics.mean(inclinaciones))
# print(inclinaciones)

#%% Ejercicio 3.23
# Especie con ejemplar mas inclinado

def especimen_mas_inclinado(lista_arboles):
    """
    Devuelve la especie que tiene al ejemplar mas inclinado y su inclinación
    dentro de una lista de arboles.
    """
    lista_especies = especies(lista_arboles)
    MAX_incl = 0
    MAX_incl_especie = ''
    for especie in lista_especies:
         max_incl = max(obtener_inclinaciones(lista_arboles, especie))
         if max_incl > MAX_incl:
             MAX_incl = max_incl
             MAX_incl_especie = especie
    return (MAX_incl, MAX_incl_especie)
        
    
# parque = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ') 
# print(especimen_mas_inclinado(parque))

#%% Ejercicio 3.24
# Especie mas inclinada en promedio

def especie_promedio_mas_inclinada(lista_arboles):
    """
    Devuelve la especie que tiene en promedio a los ejemplares mas inclinados
    y su inclinación promedio, dentro de una lista de arboles.
    """
    lista_especies = especies(lista_arboles)
    MAX_mean_incl = 0
    MAX_mean_incl_especie = ''
    for especie in lista_especies:
         mean_incl = statistics.mean(obtener_inclinaciones(lista_arboles, especie))
         if mean_incl > MAX_mean_incl:
             MAX_mean_incl = mean_incl
             MAX_mean_incl_especie = especie
    return (MAX_mean_incl, MAX_mean_incl_especie)

# parque = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ') 
# print(especie_promedio_mas_inclinada(parque))

#%% Preguntas Extra
# ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado 
# de toda la ciudad y no solo de un parque? 

def leer_ciudad(nombre_archivo):
    """
    Abre un archivo de arboles y devuelve los arboles de la ciudad.
    Devuelve una lista de diccionarios, donde cada diccionario representa un
    arbol. Dentro de cada arbol, las claves son los headers del archivo y los
    valores son los correspondientes a ese arbol.
    Los valores numéricos se convierten a int o a float segun corresponda.
    """
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        lista = []
        for row in rows:
            for i, item in enumerate(row):
                if item.isdigit():
                    row[i] = int(item)
                elif item.replace('-', '').replace('.', '').isdigit():
                    row[i] = float(item)
            lista.append(dict(zip(headers,row)))
    return lista

# ciudad = leer_ciudad('../Data/arbolado.csv')
# print(especimen_mas_inclinado(ciudad))

# ¿Podrías dar la latitud y longitud de ese ejemplar? 

def especimen_mas_inclinado_coord(lista_arboles):
    """
    Devuelve la especie que tiene al ejemplar mas inclinado, su inclinación y 
    sus coordenadas geográficas(lat, long) dentro de una lista de arboles. 
    """
    
    MAX_incl = 0
    MAX_incl_especie = ''
    for arbol in lista_arboles:
        if arbol['inclinacio'] > MAX_incl:
            MAX_incl = arbol['inclinacio']
            MAX_incl_especie = arbol['nombre_com']
            MAX_incl_lat = arbol['lat']
            MAX_incl_long = arbol['long']
    return (MAX_incl, MAX_incl_especie, MAX_incl_lat, MAX_incl_long)

# print(especimen_mas_inclinado_coord(ciudad))
    

# ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? 
# ¿De qué especie es?

def especimen_mas_alto_coord(lista_arboles):
    """
    Devuelve la especie que tiene al ejemplar mas alto, su altura y 
    sus coordenadas geográficas(lat, long) dentro de una lista de arboles. 
    """
    
    MAX_altura = 0
    MAX_altura_especie = ''
    for arbol in lista_arboles:
        if arbol['altura_tot'] > MAX_altura:
            MAX_altura = arbol['altura_tot']
            MAX_altura_especie = arbol['nombre_com']
            MAX_altura_lat = arbol['lat']
            MAX_altura_long = arbol['long']
    return (MAX_altura, MAX_altura_especie, MAX_altura_lat, MAX_altura_long)

# print(especimen_mas_alto_coord(ciudad))













    
    
    
    
    