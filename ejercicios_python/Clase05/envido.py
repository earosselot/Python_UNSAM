# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:27:49 2021

@author: Eduardo
"""

import random
from collections import Counter


def envido(mano):
    palos = ['oro', 'copa', 'espada', 'basto']
    envido = [[carta for carta in mano if carta[1] == palo] for palo in palos]
    puntos = 0
    for cartas in envido:
        if (len(cartas) == 1) and (7 >= cartas[0][0] > puntos):
            puntos = cartas[0][0]
        elif (1 < len(cartas) <= 3):
            puntos = 20
            for carta in cartas:
                if carta[0] < 8:
                    puntos += carta[0]
    return puntos


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor, palo) for palo in palos for valor in valores]


N = 100000
contador = Counter()
for i in range(N):
    contador[envido(random.sample(naipes, k=3))] += 1
prob = {}
prob[31] = contador[31]/N
prob[32] = contador[32]/N
prob[33] = contador[33]/N

for key, value in prob.items():
    print(f'La probabilidad de tener {key} es {value}')
