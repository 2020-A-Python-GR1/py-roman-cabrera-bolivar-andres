# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:29:27 2020

@author: Bolivar Roman
"""

import pandas as pd
import numpy as np
import sqlite3

save_path = 'artwork_data.pickle'

df = pd.read_pickle(save_path)
sub_df = df.iloc[49980:50519,:].copy()

path_excel = 'artwork_data.xlsx'
path_excel_col = 'artwork_data_cols.xlsx'

#Con index como columna
sub_df.to_excel(path_excel)

#Sin index como columna
cols = ['artist','title','year']

sub_df.to_excel(path_excel_col, columns = cols)


#Usar multiples hojas
path_excel_mt = 'artwork_data_mt.xlsx'
writer = pd.ExcelWriter(path_excel_mt, engine = 'xlsxwriter')
sub_df.to_excel(writer,sheet_name='first')
sub_df.to_excel(writer,sheet_name='second')
sub_df.to_excel(writer,sheet_name='third')
writer.save()

#Formato condicional

num_artistas = sub_df['artist'].value_counts()
path_excel_colors = 'artwork_data_colors.xlsx'
writer = pd.ExcelWriter(path_excel_colors, engine = 'xlsxwriter')
num_artistas.to_excel(writer,sheet_name = 'Artistas')
hoja_artistas = writer.sheets['Artistas']
range_cell = 'B2:B{}'.format(len(num_artistas.index) + 1)
format_artist = {
    "type" : "2_color_scale",
    "min_value" : "10",
    "min_type" : "percentile",
    "max_value" : "99",
    "max_type" : "percentile"
    }
hoja_artistas.conditional_format(range_cell,format_artist)
writer.save()



#SQL

with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas',conexion)
    
    
#JSON
sub_df.to_json('artist.json')
sub_df.to_json('artist_table.json',orient = 'table')