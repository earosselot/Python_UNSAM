# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:18:16 2021

@author: Eduardo
"""

import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x, y


N = 10000
puntos_dentro = 0
for i in range(N):
    x, y = generar_punto()
    if (x**2 + y**2) < 1:
        puntos_dentro += 1

pi = puntos_dentro/N * 4
print(pi)
