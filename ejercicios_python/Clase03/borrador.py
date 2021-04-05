# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:49:28 2021

@author: Eduardo
"""

import csv
        

def leer_camion(nombre_archivo):
    """
    Función que abre un archivo con el contenido de un camion, lo lee y devuelve
    la información como una lista de diccionarios.
    """
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            dicccionario = {}
            dicccionario['nombre'] = row[0]
            dicccionario['cajones'] = int(row[1])
            dicccionario['precio'] = float(row[2])
            camion.append(dicccionario)
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


def hacer_informe(dic_camion, dic_precios):
    valores =[]
    for s in dic_camion:
        valores = list(s.values())   #para quedarme con los valores de cada clave, todo junto sin las claves, en formato lista de listas

        for item in dic_precios:
            if s['nombre']==item:
                
                precio_venta = float(dic_precios[item])
                cambio=round(precio_venta-s['precio'],2)
                valores.append(cambio)  
                print('valores: ', valores)
    return valores
    

dic_camion = leer_camion('../Data/camion.csv')
dic_precio = leer_precios('../Data/precios.csv')
informe_final = hacer_informe(dic_camion,dic_precio)
print(informe_final) 
   
for r in informe_final:
    print(r)