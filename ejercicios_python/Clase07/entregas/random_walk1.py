import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def ultimo_min(lista):
    indice_min = 0
    for i in range(len(lista)):
        if abs(lista[i][-1]) < abs(lista[indice_min][-1]):
            indice_min = i
    return indice_min


def ultimo_max(lista):
    indice_max = 0
    for i in range(len(lista)):
        if abs(lista[i][-1]) > abs(lista[indice_max][-1]):
            indice_max = i
    return indice_max


N = 100000
caminatas = []
for _ in range(12):
    caminatas.append(randomwalk(N))


plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(2, 1, 1)
for caminata in caminatas:
    plt.plot(caminata)
plt.title('12 caminatas al azar')

plt.subplot(2, 2, 3)
indice_max = ultimo_max(caminatas)
plt.title('La caminata que más se aleja')
plt.plot(caminatas[indice_max])

plt.subplot(2, 2, 4)
indice_min = ultimo_min(caminatas)
plt.title('La caminata que menos se aleja')
plt.plot(caminatas[indice_min])

plt.show()
