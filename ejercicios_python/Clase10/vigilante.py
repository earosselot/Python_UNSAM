import os
import time
import informe

def vigilar(nombre_archivo):
    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)  # Mover el índice 0 posiciones desde el EOF

    while True:
        _line = f.readline()
        if _line == '':
            time.sleep(0.5)  # Esperar un rato y
            continue  # vuelve al comienzo del while
        yield _line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    camion = informe.leer_camion('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
