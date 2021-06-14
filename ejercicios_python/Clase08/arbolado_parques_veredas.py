import pandas as pd
import os

# apertura de datasets
directorio = '../Data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_veredas = os.path.join(directorio, archivo_veredas)
fname_parques = os.path.join(directorio, archivo_parques)
df_veredas = pd.read_csv(fname_veredas)
df_parques = pd.read_csv(fname_parques)

# seleccion de especie y caracteristicas
cols_veredas = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
cols_parques = ['altura_tot', 'diametro', 'nombre_cie']

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()

# unificacion de nombres de ambos dataFrames
df_tipas_veredas = df_tipas_veredas.rename(columns={'nombre_cientifico': 'nombre_cie', 'altura_arbol': 'altura_tot', 'diametro_altura_pecho': 'diametro'})

# Nueva columna ambiental
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'

# Union de datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Graficos
df_tipas.boxplot('diametro', by='ambiente')
df_tipas.boxplot('altura_tot', by='ambiente')

# 7. Habría que cambiar la especie únicamente. Se puede hacer una función, pero teniendo en cuenta las diferencias en
# el nombrado de especies en ambos dataFrames
