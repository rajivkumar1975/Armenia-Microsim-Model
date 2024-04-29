# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 06:24:36 2024

@author: wb395723
"""

import numpy as np
import pandas as pd
import os


CUR_PATH = os.path.abspath(os.path.dirname(__file__))
file1 = 'cit_data_cambodia.csv'
file2 = 'cfdata.csv'

path1 = os.path.join(CUR_PATH, file1)
taxdata = pd.read_csv(path1, index_col='Year')
cols=[]
for i in range(1, 11):
    cols += ['Loss_lag'+str(i)]
    
taxdata = taxdata.drop(columns=cols)

path2 = os.path.join(CUR_PATH, file2)
cfdata = pd.read_csv(path2, index_col='Year')

taxdf = taxdata.merge(cfdata, how="outer", on='id_n')

taxdf.to_csv('datanew.csv', index=False)