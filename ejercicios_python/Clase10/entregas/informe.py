import fileparse
import formato_tabla
from lote import Lote
import sys
from camion import Camion


def leer_camion(nombre_archivo):
    """
    Función que abre un archivo con el contenido de un camion, lo lee y
    devuelve la información como una lista de diccionarios.
    """
    camion_dicts = fileparse.parse_csv(nombre_archivo, types=[str, int, float], has_headers=True)
    camion = [Lote(c['nombre'], c['cajones'], c['precio']) for c in camion_dicts]
    return Camion(camion)


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
        costo_total += fruta.costo()
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
    informe = []
    for fruta in camion:
        diferencia = precios_venta[fruta.nombre] - fruta.precio
        elemento = (fruta.nombre, fruta.cajones, fruta.precio,
                    diferencia)
        informe.append(elemento)
    return informe


def imprimir_informe(data_informe, formateador):
    """
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia).
    """

    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
    return None


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    """
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    """
    # Leer archivos con datos
    precios = leer_precios(nombre_archivo_precios)
    camion = leer_camion(nombre_archivo_camion)

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    return None


def main(argv):
    if len(argv) == 4:
        informe_camion(argv[1], argv[2], argv[3])
    else:
        informe_camion(argv[1], argv[2])


if __name__ == '__main__':
    if 2 >= len(sys.argv) or len(sys.argv) >= 5 :
        print('Se requieren al menos 2 parámentros: archivo_camion archivo_precios')
    else:
        main(sys.argv)
