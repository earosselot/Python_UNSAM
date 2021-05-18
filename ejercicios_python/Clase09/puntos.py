class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)

class Rectangulo():
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto1.x - self.punto2.x)

    def altura(self):
        return abs(self.punto1.y - self.punto2.y)

    def area(self):
        return self.base() * self.altura()

    def __repr__(self):
        return f'Rectangulo(Punto1({self.punto1.x}, {self.punto1.y}), Punto2({self.punto2.x}, {self.punto2.y}))'

    def __str__(self):
        return f'(({self.punto1.x}, {self.punto1.y}), ({self.punto2.x}, {self.punto2.y}))'

    def desplazar(self, punto):
        self.punto1 += punto
        self.punto2 += punto

    def rotar(self):
        inferior = min(self.punto1.y, self.punto2.y)
        derecha = max(self.punto1.x, self.punto2.x)
        self.punto1 = Punto(derecha + self.altura(), inferior + self.base())
        self.punto2 = Punto(derecha, inferior)




a = Punto(0, 0)
b = Punto(1, 2)
c = Punto(3, 2)
rec = Rectangulo(a, b)
print(rec)
rec.rotar()
print(rec)

