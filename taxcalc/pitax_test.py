# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:39:29 2024

@author: wb395723
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def PIT(income, threshold, max_income, step, max_rate):
    repeats = (max_income - threshold)/step
    income_arr = np.repeat(step, repeats)
    step_rate = max_rate / repeats
    print('len of step_rate', step_rate)
    rate_arr = np.arange(0, max_rate+step_rate, step_rate)
    pitax_maxinc = sum(x * y/100 for x, y in zip(income_arr, rate_arr))
    print('pitax on max income is : ', pitax_maxinc)
    # print(income_arr)
    print('len of rate_arr', len(rate_arr))
        
    pitax = []
    etr = []
    for inc in income:
        #print('income is ', inc)
        if inc < threshold:
            pitax += [0]
            etr += [0]
        elif inc < max_income:
            size = int(round((inc - threshold)/step, 0))
            print('size is' , size)
            inc_arr = income_arr[0:size]
            ratearr = rate_arr[0:size]
            print('len of ratearr',  len(ratearr))
            tax = sum(x * y/100 for x, y in zip(inc_arr, ratearr))
            if tax < 1000:
                pitax += [0]
                etr += [0]
            else:
                pitax += [tax]
                etr += [tax/inc]
        else:
            tax = pitax_maxinc + (inc - max_income)*max_rate/100
            pitax += [tax]
            etr += [tax/inc]
    print('pitax is ', pitax)
    print('etr is', etr)
    return (pitax, etr)

income = np.arange(0, 2.5e+6, 1000)
(pitax, etr) = PIT(income, 250000, 2500000, 1000, 40)
plt.plot(income, etr)
plt.show()
