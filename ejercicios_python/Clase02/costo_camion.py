# Ejercicio 2.2
# Lectura de un archivo de datos
"""Programa que abre el archivo, lee las lineas y calcula el precio pagado por
los cajones cargados en el camion"""


# with open('../Data/camion.csv', 'rt') as f:
#     next(f)
#     frutas = []
#     for line in f:
#         row = line.split(',')
#         row[1] = int(row[1])
#         row[2] = float(row[2])
#         frutas.append(row)

# costo_total = 0
# for fruta in frutas:
#     costo_total += (fruta[1] * fruta[2])
# print(f'Costo total {costo_total}')


# ----------------------------------------------------------------------------


# Ejercicio 2.6
# Transformar un script en una función


# def costo_camion(nombre_archivo):
#     """
#     Funcion que recibe un nombre de archivo como entrada, lee la informacion sobre 
#     los cajones que cargo el camion y devuelve el costo de la carga de frutas como 
#     una variable de punto flotante.
#     """

#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         next(f)
#         frutas = []
#         for line in f:
#             row = line.split(',')
#             row[1] = int(row[1])
#             row[2] = float(row[2])
#             frutas.append(row)

#     costo_total = 0
#     for fruta in frutas:
#         costo_total += (fruta[1] * fruta[2])
    
#     return costo_total

# costo = costo_camion('../Data/camion.csv')
# print(f'Costo total {costo}')


# ----------------------------------------------------------------------------


# Ejercicio 2.8
# Administración de errores


# def costo_camion(nombre_archivo):
#     """
#     Funcion que recibe un nombre de archivo como entrada, lee la informacion sobre 
#     los cajones que cargo el camion y devuelve el costo de la carga de frutas como 
#     una variable de punto flotante.
#     Atrapa errores en el archivo si faltan datos, imprime un warning y continua
#     corriendo.
#     """

#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         next(f)
#         frutas = []
#         for line in f:
#             row = line.split(',')
#             try:
#                 row[1] = int(row[1])
#             except ValueError:
#                 print(f'Warning: {row[0]} no tiene un precio válido')
#             try:
#                 row[2] = float(row[2])
#             except:
#                 print(f'Warning: {row[0]} no posee una cantidad de cajones')

#             frutas.append(row)

#     costo_total = 0
#     for fruta in frutas:
#         try:
#             costo_total += (fruta[1] * fruta[2])
#         except TypeError:
#             print(f'Warning: {fruta[0]} no tiene un precio válido y no se sumará al costo total')
    
#     return costo_total

# costo = costo_camion('../Data/missing.csv')
# print(f'Costo total {costo}')


# python costo_camion.py 
#
# Warning: Mandarina no tiene un precio válido
# Warning: Naranja no tiene un precio válido
# Warning: Mandarina no tiene un precio válido y no se sumará al costo total
# Warning: Naranja no tiene un precio válido y no se sumará al costo total
# Costo total 30381.15


# ----------------------------------------------------------------------------


# Ejercicio 2.9
# Funciones de la biblioteca

import csv

def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion 
    sobre los cajones que cargo el camion usando el modulo csv y devuelve el 
    costo de la carga de frutas como una variable de punto flotante.
    Si faltan datos en el archivo, imprime un warning y continua corriendo.
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    next(rows)
    frutas = []
    for row in rows:
        try:
            row[1] = int(row[1])
        except ValueError:
            print(f'Warning: {row[0]} no tiene un precio válido')
        try:
            row[2] = float(row[2])
        except:
            print(f'Warning: {row[0]} no posee una cantidad de cajones')

        frutas.append(row)
    
    f.close()
    
    costo_total = 0
    for fruta in frutas:
        try:
            costo_total += (fruta[1] * fruta[2])
        except TypeError:
            print(f'Warning: {fruta[0]} no tiene un precio válido y no se sumará al costo total')
    
    return costo_total


costo = costo_camion('../Data/camion.csv')
print(f'Costo total {costo}')
# Costo total 47671.15
