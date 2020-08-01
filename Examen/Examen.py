# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:09:01 2020

@author: Bolivar Roman
"""

import numpy as np
import pandas as pd

# 2
vec = np.zeros(10)

# 3
vec_one = np.zeros(10)
vec_one[4] = 1

# 4
vec_two = np.arange(50)
vec_inv = vec_two[::-1]

# 5
mat = np.arange(9).reshape(3,3)

# 6
arreglo = np.array([1,2,0,0,4,0])
indexes = np.where(arreglo != 0)[0]

# 7
mat_iden = np.identity(3)

# 8
rand_mat = np.random.randint(10,size=(3,3,3))

# 9
matriz = np.arange(100).reshape((10,10))
menor = matriz.min()
mayor = matriz.max()

# 10
def chkImg(img): 
    if len(img) < 0:
        res = True
    res = all(ele == img[0] for ele in img) 
    return res

img = np.random.randint(255,size=(100,100,3))
arr = img.reshape(-1, img.shape[2])
color = [chkImg(arr[0]) for arr[0] in arr]
print(color.count(True))

# 11
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

ser_list = pd.Series(mylist)
ser_arr = pd.Series(myarr)
ser_dict = pd.Series(mydict)

# 12
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice

df = pd.DataFrame(ser)
df.index = df['indexCol']

# 13
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
dataframe = pd.DataFrame(ser1)
dataframe['col2'] = ser2.values


# 14
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
res = pd.concat([ser1,ser2,ser2]).drop_duplicates(keep=False)

# 15
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
res = pd.concat([ser1,ser2]).drop_duplicates(keep=False)

# 16
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()

# 17
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
df = pd.DataFrame(ser,columns=["a"])
count = df["a"].value_counts()
count.sort_values()
values = count.head(2).index
df[(df != values[0]) & (df != values[1])] = 0

# 18
ser = pd.Series(np.random.randint(1, 10, 35))
df = pd.DataFrame(ser.values.reshape(7,5))

# 19
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
print(ser[pos])

# 20
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
df = pd.DataFrame(ser1)

#Añadir vertical
df[1] = ser1

#Añadir horizontal
df = df.append(ser2,ignore_index=True)


# 21
#`groupby` tambien esta disponible en series.
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']
# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64
pesos.groupby(frutas).mean()


# 22
#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.
path = 'BostonHousing.csv'
cols = ['crim','zn','indus','chas','nox']
df2 = pd.read_csv(path, nrows = 10, usecols=cols)