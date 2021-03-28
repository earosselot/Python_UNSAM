# ----------------------------------------------------------------------------


# Ejercicio 2.10
# Ejecución desde la línea de comandos con parámetros

import csv
import sys

def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion 
    sobre los cajones que cargo el camion usando el modulo csv y devuelve el 
    costo de la carga de frutas como una variable de punto flotante.
    Atrapa errores en el archivo si faltan datos, imprime un warning y continua
    corriendo.
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    next(rows)
    frutas = []
    for row in rows:
        try:
            row[1] = int(row[1])
        except ValueError:
            print(f'Warning: {row[0]} no tiene un precio válido')
        try:
            row[2] = float(row[2])
        except:
            print(f'Warning: {row[0]} no posee una cantidad de cajones')

        frutas.append(row)
    
    f.close()
    
    costo_total = 0
    for fruta in frutas:
        try:
            costo_total += (fruta[1] * fruta[2])
        except TypeError:
            print(f'Warning: {fruta[0]} no tiene un precio válido y no se sumará al costo total')
    
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print(f'Costo total {costo}')



# bash $ python camion_commandline.py
# Costo total 47671.15


# bash $ python camion_commandline.py ../Data/missing.csv
# Warning: Mandarina no tiene un precio válido
# Warning: Naranja no tiene un precio válido
# Warning: Mandarina no tiene un precio válido y no se sumará al costo total
# Warning: Naranja no tiene un precio válido y no se sumará al costo total
# Costo total 30381.15