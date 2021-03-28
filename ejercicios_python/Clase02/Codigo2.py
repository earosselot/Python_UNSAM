import csv

def leer_camion(nombre_archivo):
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        
        camion = []
            
        for row in rows:
            
            lote = {}
            lote['nombre'] = row[0]
            lote['cajones'] = int(row[1])
            lote['precio'] = float(row[2])
            camion.append(lote)
                
    return camion

def leer_precios(nombre_archivo):
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        
        precios = {}
                   
        for row in rows:
                
            try:
                precios[row[0]] = float(row[1])
            except:
                print('Dato invalido detectado en lista de precios')
        
            
    return precios



camion_list = leer_camion('../Data/camion1.csv')
precios_dic = leer_precios('../Data/precios.csv')

costo_camion = 0
ventas = 0
ganancias = 0

for fruta in camion_list:
    costo_camion += fruta['cajones']*fruta['precio']
    ventas += fruta['cajones']*precios_dic[fruta['nombre']]
    
    
ganancias = ventas - costo_camion 
ganancias = round(ganancias,2)

print('Costo total del camion = ',costo_camion,' | Ventas totales = ',ventas , ' | Ganancias = ', ganancias)