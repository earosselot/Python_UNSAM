from vigilante import vigilar
import sys
import formato_tabla
import informe
import csv


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dict(rows, ['nombre', 'precio', 'volumen'])
    return rows


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row


def ticker(camionFile, logFile, fmt='txt'):
    camion = informe.leer_camion(camionFile)
    rows = parsear_datos(vigilar(logFile))
    rows = filtrar_datos(rows, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        rowdata = [row['nombre'], f'{row["precio"]:0.2f}', str(row['volumen'])]
        formateador.fila(rowdata)


if __name__ == '__main__':
    if len(sys.arvg) == 3:
        ticker(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        ticker(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('se requieren 2 o 3 argumentos')
