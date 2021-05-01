# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 22:47:10 2021

@author: Eduardo
"""

# %% Ejercicio 6.1
# Propagar por vecinos

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i, e in enumerate(l):
        # si esta prendido, no es el ultimo y el siguiente esta nuevo:
        if e == 1 and i < n-1 and l[i+1] == 0:
            l[i+1] = 1
            modif = True
        # si esta prendido, no es el primero y el anterior esta nuevo:
        if e == 1 and i > 0 and l[i-1] == 0:
            l[i-1] = 1
            modif = True
    return modif


def propagar(l):
    m = l.copy()
    veces = 0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")
    print(f"Y obtuve  {l}")
    return m

# %%

propagar([0, 0, 0, 0, 1])
propagar([0, 0, 1, 0, 0])
propagar([1, 0, 0, 0, 0])

# 1. No causan indexError porque las condiciones de los if chequean primero que
# no se encuentre en los casos extremos y despues compara el l[i+1] e l[i-1]
# respectivamente

# 2. Porque el algoritmo reocrre la lista del primero al ultimo y propaga a los
# dos vecinos. Cuando llega al final tiene que volver a mirar todas las
# posiciones para ver si hay vecinos a los cuales propagar.

# 3. El maximo de veces que se repite el ciclo while es n-1. Creo que hace O(n).
# Como máximo hace O(n*(n-1)) operaciones. La complejidad es cuadrática.


# %% Ejercicio 6.2
# Propagar por como el auto fantastico


def propagar_a_derecha(l):
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n-1:
            if l[i+1] == 0:
                l[i+1] = 1
    return l


def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]


def propagar(l):
    lp = l.copy()
    return propagar_a_derecha(propagar_a_izquierda(lp))


# %%

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ", l)
print("Porpagando...")
lp = propagar(l)
print("Estado original:  ", l)
print("Estado propagado: ", lp)

# 1. Porque se pasó como parámetro y se retornó. (?)

# 2. Cuando se pasó como parámetro en propagar_a_derecha se modificó l, ahí se
# modificó. Despues cuando se propaga_a_izquierda ya no se pasa como parámetro,
# entonces no se modifica.

# 4. propagar_a_derecha hace O(n) operaciones como máximo.

# 5. Creo que es O(n), 2*n para cada lado y 2*n para invertir 2 veces.


# %% Ejercicio 6.3
# Propagar con cadenas


def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)


#%%

l = [0, 0, 0, -1, -1, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
lp = propagar(l)
print("Estado original:  ", l)
print("Estado propagado: ", lp)


# 1. Porque la instrucción ps=''.join(PW) deja las x afuera.

# 2. W = s.split('x')

# 3. trad2s recorre la lista O(n). PW recorre la lista, la función in debe ser
# lineal porque la lista no está ordenada, asique O(n). La función trad2l
# es lineal porque recorre la el string 1 vez, O(n).
# El orden es O(n**3)

