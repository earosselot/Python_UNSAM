import sys
import informe_funciones


def costo_camion(nombre_archivo):
    """
    Funcion que recibe un nombre de archivo como entrada, lee la informacion
    sobre los cajones que cargo el camion y devuelve el costo de la carga de
    frutas como una variable de punto flotante.
    """
    frutas = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0
    for fruta in frutas:
        costo_total += (fruta['cajones'] * fruta['precio'])
    return costo_total


def main(argv):
    costo = costo_camion(argv[1])
    print(f'Costo total {costo}')


if __name__ == '__main__':
    main(sys.argv)
