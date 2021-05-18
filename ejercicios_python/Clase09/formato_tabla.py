# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''Crea el encabezado de una tabla.'''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''Crea una única fila de datos de la tabla'''
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    """
    Generar una tabla en formato TXT
    """
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    """
    Generar tabla en formato CSV
    """
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
    """
    Generar una tabla en formato HTML
    """
    def encabezado(self, headers):
        print(f'<tr><th>{headers[0]}</th><th>{headers[1]}</th><th>{headers[2]}</th><th>{headers[3]}</th></tr>')

    def fila(self, data_fila):
        print(f'<tr><td>{data_fila[0]}</td><td>{data_fila[1]}</td><td>{data_fila[2]}</td><td>{data_fila[3]}</td></tr>')


def crear_formateador(nombre):
    """
    crea un objeto formateador de la clase indicada por el nombre
    """
    if nombre == 'txt':
        return FormatoTablaTXT()
    elif nombre == 'csv':
        return FormatoTablaCSV()
    elif nombre == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
