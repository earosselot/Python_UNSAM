class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return len(self.items) == 0


class TorreDeControl():
    def __init__(self):
        self.cola_de_arribos = Cola()
        self.cola_de_despegues = Cola()

    def nuevo_arribo(self, numero_de_vuelo):
        self.cola_de_arribos.encolar(numero_de_vuelo)
        return None

    def nueva_partida(self, numero_de_vuelo):
        self.cola_de_despegues.encolar(numero_de_vuelo)
        return None

    def ver_estado(self):
        if self.cola_de_arribos.items:
            string_arribos = 'Vuelos esperando para aterrizar: '
            string_arribos += ', '.join(self.cola_de_arribos.items)
            print(string_arribos)
        if self.cola_de_despegues.items:
            string_despegues = 'Vuelos esperando para despegar: '
            string_despegues += ', '.join(self.cola_de_despegues.items)
            print(string_despegues)
        return None

    def asignar_pista(self):
        if self.cola_de_arribos.items:
            arribo = self.cola_de_arribos.desencolar()
            print(f'El vuelo {arribo} aterrizó con éxito.')
        elif self.cola_de_despegues.items:
            despegue = self.cola_de_despegues.desencolar()
            print(f'El vuelo {despegue} despegó con éxito')
        else:
            print('No hay vuelos en espera')
        return None



torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.ver_estado()