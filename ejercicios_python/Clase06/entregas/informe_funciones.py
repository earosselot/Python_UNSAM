# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:16:46 2021

@author: Eduardo
"""


import fileparse


def leer_camion(nombre_archivo):
    """
    Función que abre un archivo con el contenido de un camion, lo lee y
    devuelve la información como una lista de diccionarios.
    """
    camion = fileparse.parse_csv(nombre_archivo, types=[str, int, float],
                                 has_headers=True)
    return camion


def leer_precios(nombre_archivo):
    """
    Genera, a partir de un archivo de frutas y precios, un diccionario donde
    las claves son los nombres de las frutas y los valores son los precios
    """
    precios_venta = fileparse.parse_csv(nombre_archivo, types=[str, float],
                                        has_headers=False)
    return dict(precios_venta)


def costo_camion(camion):
    """
    Devuelve el costo total del camión ingresado como parámetro. El camión debe
    ser ingresado como una lista de diccionarios con las claves 'nombre',
    'cajones' y 'precio'.
    """

    costo_total = 0
    for fruta in camion:
        costo_total += fruta['cajones'] * fruta['precio']
    return costo_total


def buscar_precio(fruta, precios_venta):
    """
    Busca y devuelve el precio de una fruta dentro del diccionario
    precios_venta. Si no hay precio devuelve None.
    """
    if fruta in precios_venta:
        return precios_venta[fruta]
    else:
        return None


def vender(camion, precios_venta):
    """
    Devuelve el dinero que se genera al vender el camión de verduras al precio
    de venta.
    """
    dinero_venta = 0
    for fruta in camion:
        precio_fruta_venta = buscar_precio(fruta['nombre'], precios_venta)
        dinero_venta += fruta['cajones'] * precio_fruta_venta
    return dinero_venta


def hacer_informe(camion, precios_venta):
    """
    Devuelve una lista de tuplas con el 'nombre', 'cajones', 'precio' y
    'precio_venta - precio'
    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    informe = []
    for fruta in camion:
        elemento = ()
        diferencia = precios_venta[fruta['nombre']] - fruta['precio']
        elemento = (fruta['nombre'], fruta['cajones'], fruta['precio'],
                    diferencia)
        informe.append(elemento)
    return informe, headers


def imprimir_informe(informe, headers):
    """
    Función que imprime un informe en forma de tabla.
    """
    print(f'%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ')*len(headers))
    for r in informe:
        precio = '${:>.2f}'.format(r[2])
        print(f'{r[0]:>10} {r[1]:>10d} {precio:>10} {r[3]:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    """Función que a partir de un archivo de entrada de un camion y de precios
    genera un informe en forma de tabla por consola."""
    precios_venta = leer_precios(nombre_archivo_precios)
    camion = leer_camion(nombre_archivo_camion)
    # total_costo = costo_camion(camion)
    # total_venta = vender(camion, precios_venta)
    informe, headers = hacer_informe(camion, precios_venta)
    imprimir_informe(informe, headers)
    return None


# informe_camion('../Data/camion.csv', '../Data/precios.csv')
