# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:37:16 2021

@author: Eduardo
"""
# %% Ejercicio 5.1
# Generala Servida


import random


def tirar(n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1, 6))
    return tirada


def es_generala(tirada):
    return min(tirada) == max(tirada)

# N = 10000000
# G = sum([es_generala(tirar()) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# %% Ejercicio 5.2
# Generala no necesariamente servida

import random


def tirar(n):
    """
    Devuelve una lista que simula la tirada de n dados.
    """
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1, 6))
    return tirada


def es_generala(tirada):
    """
    Comprueba que todos los numeros de la lista son iguales. Devuelve True
    si son todos iguales.
    """
    return min(tirada) == max(tirada)


def numero_mas_repetido(lista):
    """
    Devuelve el (primer) numero que mas se repite en una lista y la cantidad
    de veces.
    Ej.:
        numero_mas_repetido([1, 2, 3, 4, 4])    # (4, 2)
        numero_mas_repetido([3, 2, 3, 4, 4])    # (3, 2)
    """
    n = 0
    elem = 0
    for e in lista:
        if lista.count(e) > n:
            n = lista.count(e)
            elem = e
    return (elem, n)


def jugar():
    """
    Simula un turno de generala hasta obtener generala o tirar 3 veces.
    """
    tirada = tirar(5)
    tiros = 1
    while (not(es_generala(tirada))) and (tiros < 3):
        num, n = numero_mas_repetido(tirada)
        tirada = tirar(5-n) + [num] * n
        tiros += 1
    if(es_generala(tirada)):
        return True
    else:
        return False


def jugar2():
    """
    Simula un turno de generala hasta obtener generala o tirar 3 veces.
    Si en las tiradas no hay numeros repetidos, tira todos los dados
    nuevamente.
    """
    tirada = tirar(5)
    tiros = 1
    while (not(es_generala(tirada))) and (tiros < 3):
        num, n = numero_mas_repetido(tirada)
        if n == 1:
            tirada = tirar(5)
        else:
            tirada = tirar(5-n) + [num] * n
        tiros += 1
    if(es_generala(tirada)):
        return True
    else:
        return False


# Caso cuando salen todos distintos quedarte con uno de los dados y tirar los
#    otros cuatro.
prob = []
for j in range(30):
    N = 100000
    G = sum([jugar() for i in range(N)])
    prob.append(G/N)
avg_prob = sum(prob)/30


print(f'La probabilidad promedio obtenida para sacar generala en tres tiros para 30 experimentos de {N} tiradas es de {avg_prob:.6f}')
# La probabilidad promedio obtenida para sacar generala en tres tiros para 30 experimentos de 100000 tiradas es de 0.045945


# Caso cuando salen todos distintos quedarte con uno de los dados y tirar
#    todos los dados de nuevo.
prob = []
for j in range(30):
    N = 100000
    G = sum([jugar2() for i in range(N)])
    prob.append(G/N)
avg_prob = sum(prob)/30


print(f'La probabilidad promedio obtenida para sacar generala en tres tiros para 30 experimentos de {N} tiradas es de {avg_prob:.6f}')
# La probabilidad promedio obtenida para sacar generala en tres tiros para 30 experimentos de 100000 tiradas es de 0.046083

