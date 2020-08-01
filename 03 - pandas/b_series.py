# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:40 2020

@author: Bolivar Roman
"""

import numpy as np
import pandas as pd

"""
lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_nums = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_nums)
series_d = pd.Series([
    True,
    False,
    10,
    "Bolivar",
    {"nombre":"Bolivar"}])


lista_cuidades = ["Ambato", "Cuenca", "Loja", "Quito"]

serie_cuidad = pd.Series(lista_cuidades, index = ["A","C","L","Q"])

val_cuidad = {
    "Ibarra":10,
    "Guayaquil": 20,
    "Cuenca":30,
    "Quito":40
    }

serie_val_ciu = pd.Series(val_cuidad)
ciudades_menor_30 = serie_val_ciu < 30

#print(type(serie_val_ciu))
#print(type(ciudades_menor_30))
#print(ciudades_menor_30)

serie_val_ciu = serie_val_ciu * 1.1

serie_val_ciu["Quito"] -=50 

svc_cuadrado = np.square(serie_val_ciu)

ciudades_uno = pd.Series({
    "Montania": 300,
    "Guayaquil": 10000,
    "Quito": 200
    })

ciudades_dos = pd.Series({
    "loja": 300,
    "Guayaquil": 10000})


ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)

ciudad_concat = pd.concat([ciudades_uno,ciudades_dos]) #se repiten al unir

ciudad_concat_verify = pd.concat([ciudades_uno,ciudades_dos],verify_integrity=True) 
#verifica integridad de contenido
#pd.append() es la misma función que concat



print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2)) #primeros dos valores
print(ciudades_uno.tail(2)) #ultimos dos valores


print(ciudades_uno.sort_values(ascending=False).head(2))
print(ciudades_uno.sort_values().tail(2))

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <=5000):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15
    
    
ciudad_calculada = ciudades_uno.map(calcular)

#if - else
#cuando NO CUMPLE condicion, aplica
ciudades_uno.where(ciudades_uno < 1000, ciudades_uno * 1.05)

#integer, signed, unsigned, float
series_numeros = pd.Series(['1.0','2',3])
print(pd.to_numeric((series_numeros),downcast = 'integer'))


#ignore, coerce, raise(default)
series_numeros_err = pd.Series(['sin valor','1.0','2',3])
print(pd.to_numeric(series_numeros_err,errors='ignore'))
"""

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.groupby(frutas).mean())
