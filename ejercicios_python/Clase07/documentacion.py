# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:50:57 2021

@author: Eduardo
"""


def valor_absoluto(n):
    '''Calcula el valor absoluto de un numero

    Pre: recibe un numero
    Post: devuelve el valor absoluto.'''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(lista):
    '''Calcula la suma de los números pares de una lista

    Pre: recibe una lista de numeros
    Post: devuelve un numero, siendo la suma de los pares.'''
    res = 0
    for e in lista:
        if e % 2 == 0:  # si e es par
            res += e
        else:
            res += 0
    return res

# invariante de ciclo: res


def veces(a, b):
    '''Devuelve el resultado de la multiplicación de a * b

    Pre: recibe 2 numeros. b debe ser un entero.
    Post: devuelve un numero, siendo la multiplicación de los parametros de
    entrada.'''
    res = 0
    veces = b
    while veces != 0:
        res += a
        veces -= 1
    return res

# invariante de ciclo: res


def collatz(n):
    res = 1
    while n != 1:
        print('n: ', n)
        print('res: ', res)
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
