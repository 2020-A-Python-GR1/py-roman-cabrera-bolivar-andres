# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:18:10 2020

@author: Bolivar Roman
"""


import pandas as pd
import xlsxwriter

save_path = 'artwork_data.pickle'
df = pd.read_pickle(save_path)
sub_df = df.iloc[49980:50519,:].copy()

num_artistas = sub_df['artist'].value_counts()
range_cell = 'B2:B{}'.format(len(num_artistas.index) + 1)

book = xlsxwriter.Workbook('deber.xlsx')
sheet = book.add_worksheet()

sheet.write_column('A1',num_artistas.index)
sheet.write_column('B1',num_artistas)


chart = book.add_chart({'type': 'pie'})

chart.add_series({
    'name': 'Artwork by artist',
    'categories': '=Sheet1!$A$2:$A$12'.format(len(num_artistas.index)+1),
    'values': '=Sheet1!$B$2:$B$12'.format(len(num_artistas.index)+1),    
    })

sheet.insert_chart('D2', chart, {'x_offset': 25, 'y_offset': 10})
book.close()

