frase = 'Todos, tu también'
palabras = frase.split()
palabras_t = []


for palabra in palabras:
    if not palabra.isalpha():
        palabra = palabra[:-1]

    if palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e'
    elif len(palabra) > 1 and palabra[-2] == 'o': 
        palabra = palabra[:-2] + 'e' + palabra[-1]
    palabras_t.append(palabra)


frase_t = ' '.join(palabras_t)
print(frase_t)
