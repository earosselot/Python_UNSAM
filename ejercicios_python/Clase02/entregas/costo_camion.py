# Ejercicio 2.9
# Funciones de la biblioteca

import csv

def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion 
    sobre los cajones que cargo el camion usando el modulo csv y devuelve el 
    costo de la carga de frutas como una variable de punto flotante.
    Si faltan datos en el archivo, imprime un warning y continua corriendo.
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


costo = costo_camion('../Data/camion.csv')
print(f'Costo total {costo}')

# bash $ python costo_camion.py 
# Costo total 47671.15
