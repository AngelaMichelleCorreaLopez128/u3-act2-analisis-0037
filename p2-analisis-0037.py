import pandas as pd
import numpy as np
print("Analisis de datos Predicción de Precios de Inmuebles (Regresión) Angela Correa NC = 0037")
# Angela Correa NC = 0037
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}
df = pd.DataFrame(inmuebles)
print(df)
print("+--+-+-+-+-++- Agrupar por una sola columna Metros Cuadrados +--++-+-+-+--+-+")
agrupado= df.groupby('Metros_Cuadrados')
print(agrupado)
print("+--+-+-+-+-++- Promedio por habitaciones +--++-+-+-+--+-+")
# Agrupar por número de habitaciones
agrupado = df.groupby('Habitaciones')

# Promedio de precios por habitaciones
print("Precio promedio por habitaciones:")
print(agrupado['Precio_Miles_USD'].mean())

# Máximo de metros cuadrados por habitaciones
print("\nMáximo de metros cuadrados por habitaciones:")
print(agrupado['Metros_Cuadrados'].max())

print("+--++--+ Segunda parte Angela Correa NC = 0037 -++-+-+-++-")
print("Agregaciones múltiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Precio_Miles_USD'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("Columna House --> Tipo de casa")
df['Tipo_Casa'] = ['Pequeña', 'Mediana', 'Pequeña','Grande', 'Grande', 'Mediana']
agrupado_múltiple = df.groupby(['Habitaciones', 'Tipo_Casa'])['Precio_Miles_USD'].mean()
print(agrupado_múltiple)
print("Angela Correa NC = 0037")
