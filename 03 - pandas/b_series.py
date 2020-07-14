# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:40 2020

@author: Bolivar Roman
"""

import numpy as np
import pandas as pd

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

print(type(serie_val_ciu))
print(type(ciudades_menor_30))
print(ciudades_menor_30)

serie_val_ciu = serie_val_ciu * 1.1

serie_val_ciu["Quito"] -=50 