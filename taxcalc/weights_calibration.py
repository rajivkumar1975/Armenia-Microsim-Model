# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:51:46 2023

@author: gpetr
"""

import pandas as pd
import os
import numpy as np
import pandas as pd
import sys 
sys.path.insert(0,"C:/Simulations/ARM_8")



growthrate=1.0
weight=1.225


filename= "C:/Simulations/ARM_8/pit_armenia_full_mortgage_updated1.csv"
df=pd.read_csv(filename)


nrows = len(df)
weights_df = pd.DataFrame(index = range(nrows))

for i in range(2021, 2031):
    weights_df["WT" + str(i)] = weight
    
for i in range(2022, 2031):
    weights_df["WT" + str(i)] = weights_df["WT" + str(i - 1)] * growthrate


weights_df.to_csv("taxcalc/pit_weights_armenia_mortgage_updated.csv", index = False)

