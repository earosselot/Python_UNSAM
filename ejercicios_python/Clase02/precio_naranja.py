# # -*- coding: utf-8 -*-

# Ejercicio 2.3
# Precio de la naranja
# """Programa que abre el archivo de precios, busca el precio de la naranja y lo 
# imprime"""

# precio_naranja = 0
# with open('../Data/precios.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         if row[0] == 'Naranja':
#             precio_naranja = row[1]

# print(f'El precio de la naranja es: {precio_naranja}')


# ----------------------------------------------------------------------------


# Ejercicio 2.7
# Buscar Precios

# def buscar_precio(fruta):
#     """
#     Funcion que busca en el archivo precios el precio de la fruta recibida como 
#     parametro y lo imprime en pantalla
#     """
    
#     precio = 'sin precio'
#     with open('../Data/precios.csv', 'rt', encoding='utf8') as f:
#         for line in f:
#             row = line.split(',')
#             if row[0] == fruta:
#                 precio = float(row[1])

#     if precio != 'sin precio':
#         print(f'El precio de un cajón de {fruta} es: {precio}')
#     else:
#         print(f'{fruta} no figura en el listado de precios.')
        

# ----------------------------------------------------------------------------


# Ejercicio 2.7
# Buscar Precios


import csv
from pprint import pprint
        

def leer_precios(nombre_archivo):
    """
    Genera, a partir de un archivo de frutas y precios, un diccionario donde 
    las claves son los nombres de las frutas y los valores son los precios
    """

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        diccionario = {}
        rows = csv.reader(f)
        for row in rows:
            try:
                diccionario[row[0]] = row[1]
            except:
                print('Warning: entrada sin datos')
    return diccionario


# bash $ python -i precio_naranja.py 
# >>> precios = leer_precios('../Data/precios.csv')
# >>> precios['Naranja']
# '106.28'
# >>> precios['Mandarina'] 
# '80.89'




            

            
