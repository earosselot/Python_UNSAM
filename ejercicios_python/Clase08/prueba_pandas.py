import pandas as pd
import os
import seaborn as sns

# Lectura de datos

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

df.head()

df.columns
df.index

df[['altura_tot', 'diametro', 'inclinacio']].describe()

# %% Selección

df['nombre_com'].unique()

df['nombre_com'] == 'Ombú'

cant_ejemplares = df['nombre_com'].value_counts()


# %% Filtros booleanos

# filas
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

# columnas
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()

# filas y columnas + copy
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

# %% Graficos

df_jacarandas.plot.scatter(x='diametro', y='altura_tot')

sns.scatterplot(data=df_jacarandas, x='diametro', y='altura_tot')

