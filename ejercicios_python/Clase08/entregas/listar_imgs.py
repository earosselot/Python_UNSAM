# Escribí un programa que dado un directorio, imprima en pantalla los nombres de todos los archivos .png que se
# encuentren en algún subdirectorio del él.
#
# Observación: Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el
# directorio a leer original. En la Sección 7.3 dimos un modelo de script que te puede servir.

import os
import sys


def main(argv):
    """
    Imprime los archivos .png de un directorio y sus subdirectorios.
    """
    pngFiles = selectPngFiles(argv[1])
    for file in pngFiles:
        print(file)


def selectPngFiles(directorio):
    """
    Genera una lista solo con los archivos png de un directorio y sus subdirectorios.
    """
    allFiles = getFiles(directorio)
    pngFiles = [file for file in allFiles if file.endswith('.png')]
    return pngFiles


def getFiles(directorio):
    """
    Genera una lista con todos los archivos dentro del directorio y sus subdirectorios.
    """
    allFiles = []
    for root, dirs, files in os.walk(directorio):
        allFiles += files
    return allFiles


if __name__ == '__main__':
    main(sys.argv)
