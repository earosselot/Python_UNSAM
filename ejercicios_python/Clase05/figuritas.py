# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:53:46 2021

@author: Eduardo
"""


import random
import numpy as np
import matplotlib.pyplot as plt


# %% Ejercicio 5.9 - 12
# Figuritas sueltas

def crear_album(figus_total):
    return np.zeros(figus_total)


def album_incompleto(A):
    return 0 in A


def comprar_figu(figus_total):
    return random.randint(1, figus_total)


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cantidad_figus = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        cantidad_figus += 1
    return cantidad_figus


figus_total = 6
promedio6 = np.mean([cuantas_figus(figus_total) for i in range(1000)])
# 14.718

figus_total = 670
promedio670 = np.mean([cuantas_figus(figus_total) for i in range(100)])
# 4775.58

# %% Ejercicio 5.15 - 18
# Ejercicios con paquetes


def comprar_paquete(figus_total, figus_paquete):
    return random.choices(range(figus_total), k=figus_paquete)


comprar_paquete(15, 5)
# [10, 1, 2, 3, 15]


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu-1] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes


n_repeticiones = 100
figus_total = 670
figus_paquete = 5
promedio_paquetes = np.mean([cuantos_paquetes(figus_total, figus_paquete) 
                             for i in range(n_repeticiones)])
# 953.12
# 931.4


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

# %% Ejercicio 5.19 - 5.23
# Ejercicios un toque mas estadisticos

n_repeticiones = 1000
figus_total = 670
figus_paquete = 5
lista_paquetes = [cuantos_paquetes(figus_total, figus_paquete) 
                  for i in range(n_repeticiones)]

prob_menos_850 = sum([1 for cant in lista_paquetes if cant < 850]
                     ) / n_repeticiones

n_paquetes_hasta_llenar = np.array(figus_paquete)
(n_paquetes_hasta_llenar <= 850).sum()  # esto no entendí, devuelve 1

# %% Ejercicio 5.20
# Plotear el histograma

plt.hist(lista_paquetes, bins=35)


# %% Ejercicio 5.21

lista_paquetes_ordenados = sorted(lista_paquetes)
print(f'Para tener un 90% de probabilidades de llenar el album hay que comprar {lista_paquetes_ordenados[900]} paquetes.')

# %% Ejercicio 5.22
# Paquetes sin repetidas


def comprar_paquete_sin_repe(figus_total, figus_paquete):
    return random.sample(range(figus_total), k=figus_paquete)


comprar_paquete_sin_repe(10, 5)


def cuantos_paquetes2(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete_sin_repe(figus_total, figus_paquete)
        for figu in paquete:
            album[figu-1] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes


n_repeticiones = 100
figus_total = 670
figus_paquete = 5
promedio_paquetes = np.mean([cuantos_paquetes2(figus_total, figus_paquete)
                             for i in range(n_repeticiones)])
# 936.34
# 953.17
# 945.19


# %% Ejercicio 5.23
# Cooperar vs competir


def albumes_incompletos(album):
    i = 0
    while i < len(album):
        if album[i] < 5:
            return True
        i += 1
    return False


def cuantos_paquetes_comunidad(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad_paquetes = 0
    while albumes_incompletos(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu-1] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes / 5


n_repeticiones = 100
figus_total = 670
figus_paquete = 5
promedio_paquetes = np.mean([cuantos_paquetes_comunidad(figus_total, figus_paquete)
                             for i in range(n_repeticiones)])
# 402.58
# 395.44
