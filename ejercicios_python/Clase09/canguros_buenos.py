# Clase Canguro definida por mí

class Canguro:
    def __init__(self):
        self.contenido_marsupio = []

    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)

    def __str__(self):
        cadena = 'Canguro, lleva '
        for objeto in self.contenido_marsupio:
            cadena = cadena + f' {objeto}'
        cadena = cadena + '.'
        return cadena


# %%

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [self.nombre + ' tiene en su marsupio:']
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


# El problema consistía en que todos los objetos de la clase Canguro que no pasan el segundo argumento, van a
# compartir un puntero a la misma lista contenido en su atributo contenido_marsupio. Este no es el
# comportamiento esperado. El comportamiento esperado sería que cada canguro tenga su bolsa.
# El error se puede corregir sacando el atributo de los parámetros pedidos en la definición de clase, linea 22
# (contenido = []) y asignando al atributo self.contenido_marsupio una lsita vacía, linea 29.
