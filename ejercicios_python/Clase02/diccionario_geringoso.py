# Ejercicio 2.14
# Diccionario geringoso


def diccionario_geringoso(lista_palabras):
    """
    Función que, a partir de una lista de palabras, devuelve un diccionario
    geringoso.
    """

    dict = {}
    for palabra in lista_palabras:
        capadepenapa = ''
        for c in palabra:
            if c in 'aeiou':
                capadepenapa += c + 'p' + c
            elif c in 'AEIOU':
                capadepenapa += c + 'P' + c
            else:
                capadepenapa += c
        dict[palabra] = capadepenapa
    return dict

lista = ['banana', 'manzana', 'mandarina']
x = diccionario_geringoso(lista)
print(x)

# bash $ python  diccionario_geringoso.py
# {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}