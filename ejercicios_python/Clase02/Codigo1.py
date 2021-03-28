import csv

def leer_camion(nombre_archivo):
	f = open(nombre_archivo)
	rows = csv.reader(f, delimiter=',')
	headers = next(rows)
	lista = []	
	for row in rows:
		nombre, cajones, precio = row
		lista.append({'nombre':nombre, 'cajones':int(cajones), 'precio':float(precio)})
	return lista

def leer_precios(nombre_archivo):
	f = open(nombre_archivo)
	rows = csv.reader(f, delimiter=',')
	diccionario = {}
	for row in rows:
		try:
			diccionario[row[0]] = float(row[1])
		except:
			pass
	return diccionario


camion = leer_camion('../Data/camion1.csv')
precios = leer_precios('../Data/precios.csv')

costo_camion = 0
costo_precios = 0
for producto in camion:
	costo_camion += producto['cajones']*producto['precio']
	costo_precios += producto['cajones']*precios[producto['nombre']]

print(f'El camión costó: {costo_camion:4.2f}')
print(f'Con la venta se recaudó: {costo_precios:4.2f}')

diferencia = costo_precios - costo_camion

if costo_camion < costo_precios:
	print(f'Tuvimos ganancia de: {diferencia: 4.2f}')
else:
	print(f'Tuvimos perdida de:{diferencia: 4.2f}')
