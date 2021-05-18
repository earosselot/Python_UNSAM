# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:30:58 2021

@author: Eduardo
"""

import numpy as np
import matplotlib.pyplot as plt


def lastMin(caminatas):
    '''Devuelve el índice de la lista cuyo último número es el menor en módulo
    Pre: lista de listas de numeros enteros
    Post: indice de la lista cuyo último valor es mínimo en módulo.
    '''
    minLastIndex = 0
    for i in range(len(caminatas)):
        if abs(caminatas[i][-1]) < abs(caminatas[minLastIndex][-1]):
            minLastIndex = i
    return minLastIndex


def lastMax(caminatas):
    '''Devuelve el índice de la lista cuyo último número es el mayor en modulo
    Pre: lista de listas de numeros enteros
    Post: indice de la lista cuyo último valor es maximo en módulo.
    '''
    maxLastIndex = 0
    for i in range(len(caminatas)):
        if abs(caminatas[i][-1]) > abs(caminatas[maxLastIndex][-1]):
            maxLastIndex = i
    return maxLastIndex


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


N = 100000
caminatas = []
for _ in range(12):
    caminatas.append(randomwalk(N))

colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'b', 'k', 'm']

plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(2, 1, 1)
for i, caminata in enumerate(caminatas):
    plt.plot(caminata, color=colors[i])
plt.title('12 caminatas al azar')

plt.subplot(2, 2, 3)
maxLastIndex = lastMax(caminatas)
plt.title('La caminata que más se aleja')
plt.plot(caminatas[maxLastIndex], color=colors[maxLastIndex])

plt.subplot(2, 2, 4)
minLastIndex = lastMin(caminatas)
plt.title('La caminata que menos se aleja')
plt.plot(caminatas[minLastIndex], color=colors[minLastIndex])

plt.show()
