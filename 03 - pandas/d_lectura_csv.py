# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:46 2020

@author: Bolivar Roman
"""

import pandas as pd
import os

path = 'artwork_data.csv'
save_path = 'artwork_data.pickle'

df1 = pd.read_csv(path,nrows=10)

columns = ['id','artist','title','medium','year',
           'acquisitionYear','height','width','units']

df2 = pd.read_csv(path, nrows = 10,usecols=columns)

df3 = pd.read_csv(path, nrows = 10,usecols=columns,index_col='id')

df3.to_pickle(save_path)
df4 = pd.read_pickle(save_path)