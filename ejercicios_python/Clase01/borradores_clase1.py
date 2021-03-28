# Ejercico 1.12
# Da True porque la candena no esta vacía

# bool("False")   # True
# bool("")        # False

# -------------------------------------------------------
# Ejercico 1.17

# cadena = "Ejemplo con for"
# count = 0
# for c in cadena:
#     if c == 'o':
#         count += 1
# print(count)

# --------------------------------------------------

lista = ['a', 'b', 'x']
lista_unida = ''.join(lista)
print(lista_unida)


cadena_de_lista = ''
for c in lista:
    cadena_de_lista = cadena_de_lista + c
print(cadena_de_lista)

cadena = 'esta cadena'
lista_nueva = []
for c in cadena:
    lista_nueva.append(c)
print(lista_nueva)

print(list(cadena))