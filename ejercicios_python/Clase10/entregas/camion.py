

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, index):
        return self.lotes[index]

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __repr__(self):
        return f'Camion {self.lotes}'

    def __str__(self):
        return f'{self.lotes}'

    def precio_total(self):
        return sum([lote.costo() for lote in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
