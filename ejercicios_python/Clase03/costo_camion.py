# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:35:57 2021

@author: Eduardo
"""
# Ejercicio 3.8
# Un ejemplo practico con enumerate()

import csv

def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion 
    sobre los cajones que cargo el camion usando el modulo csv y devuelve el 
    costo de la carga de frutas como una variable de punto flotante.
    Si faltan datos en el archivo, imprime un warning indicando el numero de 
    fila con error y continua corriendo.
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    next(rows)
    frutas = []
    for n_row, row in enumerate(rows, start=1):
        try:
            row[1] = int(row[1])
            row[2] = float(row[2])
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')

        frutas.append(row)
    
    f.close()
    
    costo_total = 0
    for fruta in frutas:
        try:
            costo_total += (fruta[1] * fruta[2])
        except TypeError:
            print(f'Warning: {fruta[0]} no tiene un precio válido y no se sumará al costo total')
    
    return costo_total


costo = costo_camion('../Data/missing.csv')
print(f'Costo total {costo}')
# Costo total 47671.15

#%% Ejercicio 3.9 
# La funcion zip()

def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion 
    sobre los cajones que cargo el camion usando el modulo csv y devuelve el 
    costo de la carga de frutas como una variable de punto flotante.
    Si faltan datos en el archivo, imprime un warning indicando el numero de 
    fila con error y continua corriendo.
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    encabezados = next(rows)
    costo_total = 0
    for n_row, row in enumerate(rows, start=1):
        # record = {}
        record = dict(zip(encabezados, row))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return costo_total


costo = costo_camion('../Data/fecha_camion.csv')
print(f'Costo total {costo}')
# Costo total 47671.15

#%% Ejercicio 3.9 bis

import csv
from pprint import pprint
        

def leer_camion(nombre_archivo):
    """
    Función que abre un archivo con el contenido de un camion, lo lee y devuelve
    la información como una lista de diccionarios.
    """
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row, row in enumerate(rows, start=1):
            diccionario = {}
            diccionario = dict(zip(headers, row))
            try:
                diccionario['cajones'] = int(diccionario['cajones'])
                diccionario['precio'] = float(diccionario['precio'])
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
            camion.append(diccionario)
    return camion


def leer_precios(nombre_archivo):
    """
    Genera, a partir de un archivo de frutas y precios, un diccionario donde 
    las claves son los nombres de las frutas y los valores son los precios
    """
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        precios_venta = {}
        rows = csv.reader(f)
        for row in rows:
            try:
                precios_venta[row[0]] = float(row[1])
            except:
                print('Warning: entrada sin datos')
    return precios_venta


def costo_camion(camion):
    """
    Devuelve el costo total del camión ingresado como parámetro. El camión debe
    ser ingresado como una lista de diccionarios con las claves 'nombre', 
    'cajones' y 'precio'.
    """

    costo_total = 0
    for fruta in camion:
        costo_total += fruta['cajones'] * fruta['precio']
    return costo_total


def buscar_precio(fruta, precios_venta):
    """
    Busca y devuelve el precio de una fruta dentro del diccionario 
    precios_venta. Si no hay precio devuelve None.
    """
    if fruta in precios_venta:
        return precios_venta[fruta]
    else:
        return None


def vender(camion, precios_venta):
    """
    Devuelve el dinero que se genera al vender el camión de verduras al precio
    de venta.
    """
    dinero_venta = 0
    for fruta in camion:
        precio_fruta_venta = buscar_precio(fruta['nombre'], precios_venta)
        dinero_venta += fruta['cajones'] * precio_fruta_venta
    return dinero_venta


precios_venta = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/fecha_camion.csv')
total_costo = costo_camion(camion)
total_venta = vender(camion, precios_venta)
pprint(f'Costo camion: $ {total_costo:.2f} | Dinero por venta: $ {total_venta:.2f} | Balance: $ {total_venta - total_costo:+.2f}')

# bash $ python informe.py 
# Warning: entrada sin datos
# Costo camion: $ 47671.15 | Dinero por venta: $ 62986.10 | Balance: $ +15314.95