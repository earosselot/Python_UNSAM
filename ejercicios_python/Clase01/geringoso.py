# Ejercicio 1.18
# Geringoso rústico

cadena = 'boligoma'
capadepenapa = ''

for c in cadena:
    if c in 'aeiou':
        capadepenapa += c + 'p' + c
    else:
        capadepenapa += c

print(capadepenapa)
