# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:29:04 2021

@author: Eduardo
"""

# %% Ejercicio 5.5
# Gaussiana

import random

n = 99
mediciones_temperatura = []
for i in range(n):
    mediciones_temperatura.append(random.normalvariate(37.5, 0.2))
print(mediciones_temperatura)

print(f'El valor máximo medido fue de: {max(mediciones_temperatura)}')
print(f'El valor mínimo medido fue de: {min(mediciones_temperatura)}')
print(f'El valor promedio medido fue de: {sum(mediciones_temperatura)/n}')
mediciones_ordenadas = sorted(mediciones_temperatura)
print(f'El valor mediano medido fue de: {mediciones_ordenadas[int(n/2-0.5)]}')

# El valor máximo medido fue de: 38.01262614882437
# El valor mínimo medido fue de: 37.02742283738101
# El valor promedio medido fue de: 37.498189566687635
# El valor mediano medido fue de: 37.47305458943038

q1 = mediciones_ordenadas[int((n+1)/4-1)]
print(f'El primer cuartil es: {q1}')
q3 = mediciones_ordenadas[int(3*(n+1)/4-1)]
print(f'El tercer cuartil es: {q3}')

# El primer cuartil es: 37.351845591430795
# El tercer cuartil es: 37.61448634636062

# %% Ejercicio 5.7
# Guardar Temepraturas

import numpy as np

n = 999
mediciones_temperatura = []
for i in range(n):
    mediciones_temperatura.append(random.normalvariate(37.5, 0.2))

np.save('../Data/Temperaturas.npy', mediciones_temperatura)
    
x = np.load('../Data/Temperaturas.npy')
