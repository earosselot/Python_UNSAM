# -*- coding: utf-8 -*-
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%

# Ejercicio 3.1. Función tiene_a()
#   Comentario: El error era de tipo semantico y estaba ubicado en el return 
# dentro de la estructura if-else. Lo que en realidad esta haciendo la función
# es chekear solo la primer letra de la palabra. Otro posible error es que solo
# este mirando las a minusculas, pero no esta especificado que tiene que hacer
# la función.
#    Lo corregí agregando una variable resultado que empieza con valor False,
# y si hay alguna 'a' o 'A' en la cadena cambia el valor a True. Al final 
# devuelve el valor de la variable.
#    A continuación va el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    resultado = False
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            resultado = True
        i += 1
    return resultado

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%

# Ejercicio 3.2. Función tiene_a(), nuevamente
# Comentario: El error era de tipo sintactico y estaba ubicado en varios lugares
# Faltaban 2 puntos en los ciclos/condicionales. Un igual en la comparacion y
# Falso estaba escrito en español.
# Se soluciona agregando lo que falta y corrigiendo el falso.
#    A continuación va el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
# Ejercicio 3.3. Función tiene_uno()
#   Comentario: El error era en tiempo de ejecución y estaba ubicado en la linea 
# "n = len(expresion)".
#   Lo corregí convirtiendo la expresión a cadena antes de hacer nada
#    A continuación va el código corregido:
    
    
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))


#%%
# Ejercicio 3.4 Alcances
#   Comentario: El error es de tipo semántico. La función no devuelve nada ('None'
# por defecto). 
# Se corrige agregandole un return a la funcion.
#    A continuación va el código corregido:

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
# Ejericio 3.5 Pisando memoria
#   Comentario: El error es de tipo semantico. La función esta modificando el
# mismo diccionario muchas veces. Y luego appendeandolo a la lista. Como no 
# se reinicializa el registro = {}, las escrituras a la variable registro 
# modifican a esta y a todos los elementos de la lista, que tienen punteros 
# a la variable registro.
#   Se corrige cambiando la posicion de la linea "registro = {}" adentro del 
# for. 
#    A continuación va el código corregido:


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[] 
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("../Data/camion.csv")
pprint(camion)



