# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:18:52 2020

@author: Bolivar Roman
"""


import pandas as pd
import numpy as np
from datetime import date

"""
## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros
arr = np.random.randint(0,10,60).reshape(10,6)
df = pd.DataFrame(arr)
print(df.head(5))
print(df.tail(5))

## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

arr2 = np.random.randint(0,10,24).reshape(6,4)
cols = ['A','B','C','D']
indexes = [date.today().strftime("%Y-%m-%d"),
         date.today().strftime("%Y-%m-%d"),
         date.today().strftime("%Y-%m-%d"),
         date.today().strftime("%Y-%m-%d"),
         date.today().strftime("%Y-%m-%d"),
         date.today().strftime("%Y-%m-%d")]


df2 = pd.DataFrame(arr2, columns = cols, index = indexes)

## 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.
arr4 = np.random.randint(0,10,60).reshape(10,6)
df4 = pd.DataFrame(arr4)

cols4 = df4.columns.values

vals = df4.values


## 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe
arr5 = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr5)

desc_df5 = df5.describe()

## 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos
arr6 = np.random.randint(0,10,60).reshape(10,6)
df6 = pd.DataFrame(arr6)

df_transpuesto = df6.transpose()

"""

## 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

arr7 = np.random.randint(0,10,60).reshape(10,6)
df7 = pd.DataFrame(arr7)


## 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

arr8 = np.random.randint(1,10,60).reshape(10,6)
df8 = pd.DataFrame(arr8)

mayor_7 = df8 > 7
df_mayor7 = df8[mayor_7]


## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

arr9 = np.random.randint(1,10,60).reshape(10,6)
df9 = pd.DataFrame(arr9)
df9 = df9.where(df9 < 5)
df9.fillna(0)

## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

arr10 = np.random.randint(1,10,60).reshape(10,6)
df10 = pd.DataFrame(arr10)
media = df10.mean()
mediana = df10.median()
prom = np.average(df10)

## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

arr11 = np.random.randint(1,10,60).reshape(10,6)
df11 = pd.DataFrame(arr11)

arr_add = np.random.randint(0,10,60).reshape(10,6)
df_add = pd.DataFrame(arr_add)

df11 = df11.append(df_add)

## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

arr12 = pd.util.testing.rands_array(5, 60).reshape(10,6)
df12 = pd.DataFrame(arr12)

df12_concat = pd.DataFrame(df12[0] + df12[1])
df12_concat[1] = df12[2] + df12[3]
df12_concat[2] = df12[4] + df12[5]

## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna

arr13 = np.random.randint(1,10,60).reshape(10,6)
df13 = pd.DataFrame(arr13)

for col in df13.columns:
    print(df13[col].value_counts())
    
## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C

arr14 = np.random.randint(1,10,30).reshape(10,3)
df14 = pd.DataFrame(arr14, columns=['A','B','C'])

op = (df14['A'] * df14['B'])/df14['C']
df14['res'] = op