# ----------------------------------------------------------------------------


# Ejercicio 2.15
# Lista de tuplas


# import csv

# def leer_camion(nombre_archivo):
#     """
#     Función que abre un archivo con el contenido de un camion, lo lee y devuelve
#     la información como una lista de tuplas.
#     """
#     camion = []
#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         rows = csv.reader(f)
#         headers = next(rows)

#         for row in rows:

#             tupla = (row[0], int(row[1]), float(row[2]))
#             camion.append(tupla)
    
#     return camion

# cam = leer_camion('../Data/camion.csv')
# print(cam)

# bash $ python informe.py 
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Caqui', 150, 103.44), ('Mandarina', 200, 51.23), ('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]


# ----------------------------------------------------------------------------


# Ejercicio 2.16
# Lista de diccionarios


# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     """
#     Función que abre un archivo con el contenido de un camion, lo lee y devuelve
#     la información como una lista de diccionarios.
#     """
#     camion = []
#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
        
#         for row in rows:
#             dicccionario = {}
#             dicccionario['nombre'] = row[0]
#             dicccionario['cajones'] = int(row[1])
#             dicccionario['precio'] = float(row[2])
            
#             camion.append(dicccionario)
    
#     return camion

# cam = leer_camion('../Data/camion.csv')
# pprint(cam)

# bash $ python informe.py 
# [{'cajones': '100', 'nombre': 'Lima', 'precio': '32.2'},
#  {'cajones': '50', 'nombre': 'Naranja', 'precio': '91.1'},
#  {'cajones': '150', 'nombre': 'Caqui', 'precio': '103.44'},
#  {'cajones': '200', 'nombre': 'Mandarina', 'precio': '51.23'},
#  {'cajones': '95', 'nombre': 'Durazno', 'precio': '40.37'},
#  {'cajones': '50', 'nombre': 'Mandarina', 'precio': '65.1'},
#  {'cajones': '100', 'nombre': 'Naranja', 'precio': '70.44'}]


# ----------------------------------------------------------------------------


# Ejercicio 2.18
# Balances

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
camion = leer_camion('../Data/camion.csv')
total_costo = costo_camion(camion)
total_venta = vender(camion, precios_venta)
print(f'Costo camion: $ {total_costo:.2f} | Dinero por venta: $ {total_venta:.2f} | Balance: $ {total_venta - total_costo:+.2f}')

# bash $ python informe.py 
# Warning: entrada sin datos
# Costo camion: $ 47671.15 | Dinero por venta: $ 62986.10 | Balance: $ +15314.95





