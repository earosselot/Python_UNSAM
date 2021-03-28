# ----------------------------------------------------------------------------


# Ejercicio 2.7
# Buscar Precios

def buscar_precio(fruta):
    """
    Funcion que busca en el archivo precios el precio de la fruta recibida como 
    parametro y lo imprime en pantalla
    """
    
    precio = 'sin precio'
    with open('../Data/precios.csv', 'rt', encoding='utf8') as f:
        for line in f:
            row = line.split(',')
            if row[0] == fruta:
                precio = float(row[1])

    if precio != 'sin precio':
        print(f'El precio de un cajón de {fruta} es: {precio}')
    else:
        print(f'{fruta} no figura en el listado de precios.')


buscar_precio('Lechuga')
# El precio de un cajón de Lechuga es: 24.22
buscar_precio('Inojo')
# Inojo no figura en el listado de precios.

        

# ----------------------------------------------------------------------------