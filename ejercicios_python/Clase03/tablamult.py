# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:25:13 2021

@author: Eduardo
"""

enteros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
head = '    '
separador = '-----'
lineas = '----'
for numero in enteros:
    string = f'{numero:4}'
    head += string
    separador += lineas
    
print(head)
print(separador)

for numero in enteros:
    resultado = 0
    linea = f'{numero:>2}: '
    for numero1 in enteros:
        linea += f'{resultado:>4}'
        resultado += numero    
    print(linea)
        