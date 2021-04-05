# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:46:13 2021

@author: Eduardo
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

rta = tiene_a ('palabra')
print(rta)

#%%

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        # invertida.append (lista.pop(i))   # Paso Clave
        invertida.append(lista[i])          # Paso corregido
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
#  Entrada [1, 2, 3, 4, 5], Salida: [5, 4, 3, 2, 1]


#%%

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    # registro={}                                   # Paso Clave
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}                             # Debe ir aca
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
#  {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
#  {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
#  {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
#  {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
#  {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
#  {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
