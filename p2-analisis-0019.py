# importar librerias 
import pandas as pd
import numpy as np

print("analisis de datos del Sistema Solar Jesus Arriaga 0019")

planetas = {
    "Nombre": ["Mercurio", "Mercurio", "Tierra", "Tierra", "Júpiter"],
    "Tipo_Planeta": ["Rocoso", "Rocoso", "Rocoso", "Rocoso", "Gaseoso"],
    "Distancia_Sol_Mkm": [57.9, 108.2, 149.6, 227.9, 778.5],
    "Descubridor_Año": [1631, 1610, 0, 1610, 1610]
}

df = pd.DataFrame(planetas)
print(df)

print("-+-+-Agrupar por tipo de planeta -++-+--")
agrupado = df.groupby('Tipo_Planeta')
print(agrupado)

print("-+-+-por agregacion -++-+--")
# distancia promedio por cada tipo de planeta
print(agrupado['Distancia_Sol_Mkm'].mean())

# distancia maxima por cada tipo de planeta
print(agrupado['Distancia_Sol_Mkm'].max())