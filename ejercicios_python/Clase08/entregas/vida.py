import datetime


def segundosDeVida(fechaNacimiento):
    ahora = datetime.datetime.now()
    fechaNacimientoList = fechaNacimiento.split('/')
    dia = int(fechaNacimientoList[0])
    mes = int(fechaNacimientoList[1])
    anio = int(fechaNacimientoList[2])
    nacimiento = datetime.datetime(anio, mes, dia)
    segundosVividos = ahora - nacimiento
    return segundosVividos.total_seconds()


# print(segundosDeVida('09/04/1990'))
# 984056040.284263 segs
