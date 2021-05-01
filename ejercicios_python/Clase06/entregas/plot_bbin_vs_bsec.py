# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:37:10 2021

@author: Eduardo
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición,
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0  # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i, z in enumerate(lista):
        comps += 1  # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    comps = 0
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio      # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos, comps


def generar_lista(n, m):
    lista = random.sample(range(m), k=n)
    lista.sort()
    return lista


def generar_elemento(m):
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    """Función que hace k experimentos de busqueda secuencial en una lista de
    enteros entre 1 y m y devuelve el promedio de operaciones."""
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial(lista, x)[1]
    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    """Función que hace k experimentos de busqueda binaria en una lista de
    enteros entre 1 y m y devuelve el promedio de operaciones."""
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]
    comps_prom = comps_tot / k
    return comps_prom


n = 100
m = 10000
k = 1000

largos = np.arange(256) + 1  # estos son los largos de listas que voy a usar

# comps_promedio y comps_promedio_bin guardan el promedio de comparaciones
# sobre una lista de largo i, para i entre 1 y 256.
comps_promedio = np.zeros(256)
comps_promedio_bin = np.zeros(256)


for i, n in enumerate(largos):
    lista = generar_lista(n, m)  # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

for i, n in enumerate(largos):
    lista = generar_lista(n, m)
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)


# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_promedio_bin, label='Búsqueda Binaria')
plt.plot(largos, comps_promedio, label='Búsqueda Secuencial')
plt.ylim(0, 50)
plt.xlim(0, 50)
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
