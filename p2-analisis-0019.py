import pandas as pd
import numpy as np

print("Analisis de datos Salud | Jesus Arriaga García NC = 0019")

pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}

df = pd.DataFrame(pacientes)
print(df)

print("\n----- Agrupar por una sola columna ----- 0019")
Riesgo = df.groupby("Nivel_Riesgo")
print(Riesgo)

print("\n----- Presión Arterial Promedio por Nivel de Riesgo ----- 0019")
# Presión arterial promedio por Nivel de Riesgo
print(Riesgo["Presion_Arterial"].mean())

# Presión arterial máxima por Nivel de Riesgo
print("\n----- Presión Arterial Máxima ----- 0019")
print(Riesgo["Presion_Arterial"].max())
print('+-+-+-+Jesus Arriaga García NC = 0019-+-+-++-')
print('segun da parte')
print('agregaciones multiples')
# Se cambió 'Salary' por 'Presion_Arterial'
resultado_agregado = Riesgo['Presion_Arterial'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print('agrupacion por columnas')
print('agregar columnas al dataframe')
print('columna Grupo_Clinico --> grupo')
# Se agrega una nueva columna de categorización (Grupo A / Grupo B)
df['Grupo_Clinico'] = ['A', 'B', 'A', 'B', 'A', 'B']

# Se agrupó por 'Nivel_Riesgo' y 'Grupo_Clinico' calculando la media de 'Presion_Arterial'
agrupado_multiple = df.groupby(['Nivel_Riesgo', 'Grupo_Clinico'])['Presion_Arterial'].mean()
print(agrupado_multiple)