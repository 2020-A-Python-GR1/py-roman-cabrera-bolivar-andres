# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:26:04 2020

@author: Bolivar Roman
"""

import pandas as pd

datos = {
    
    'nota 1' : {
        
        'Pepito': 7,
        'Juanita' : 8,
        'Maria' : 9
        },
    'nota 2' : {
        
        'Pepito': 7,
        'Juanita' : 8,
        'Maria' : 9
        },
    
    'disciplina':{
        'Pepito': 4,
        'Juanita': 9,
        'Maria': 2
        },
    }

notas = pd.DataFrame(datos)

condicion_nota = notas['nota 1'] > 7
condicion_nota_dos = notas['nota 2'] > 7
condicion_disc = notas['disciplina'] > 7

mayores_siete = notas.loc[condicion_nota, ['nota 1']]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc['Maria','disciplina'] = 7
notas.loc[:,'disciplina'] = 7

prom_pepito = sum(notas.loc['Pepito',:]) /3 
prom_juanita = sum(notas.loc['Juanita',:]) /3 
prom_maria = sum(notas.loc['Maria',:]) /3 
