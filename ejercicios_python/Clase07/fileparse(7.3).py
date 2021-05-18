# -*- coding: utf-8 -*-

import csv


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el
    parámetro select, que debe ser una lista de nombres de las columnas a
    considerar. Solo se puede usar en caso de tener headers.
    Se puede especificar el tipo de datos de salida de cada columna con el
    parametro types, que debe ser una lista con los tipos de datos, ej:
        types = [str, float, int]
    Con el parámetro booleano has_headers se puede aclarar si el archivo no
    posee headers, en ese caso la salida será una lista de tuplas, en vez de
    una lista de diccionarios.
    '''
    with open(nombre_archivo, encoding='utf8') as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if has_headers and select:
            indices = [encabezados.index(nombre_columna) for nombre_columna
                       in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            if has_headers:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                # ó arma la tupla
                registro = tuple(fila)
                registros.append(registro)

    return registros


# camion = parse_csv('../Data/camion.csv')
