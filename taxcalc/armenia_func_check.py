# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:37:09 2024

@author: wb395723
"""

import pandas as pd
import numpy as py
import functions_cit_armenia as func

data = pd.read_csv('cit_data_armenia.csv')

col_list = []
for col in data.columns:
    if col[:3] == 'inc':
        col_list += [col]
col_list = col_list[:36]

args = (data['loss_natural'], data['loss_quality'], data['loss_accidental'], data['loss_other'])

func.calc_loss_fun(args)

