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
# Numero por promedio de habitaciones
print(agrupado['Habitaciones'].mean())
print("+--+-+-+-+-++-Promedio de precio de cada habitacion +--++-+-+-+--+-+")
# Precio maximo por cada habitacion
print(agrupado['Precio_Miles_USD'].max())
print("Angela Correa NC = 0037")
