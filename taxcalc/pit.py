import pandas as pd
import numpy as np


def PIT(income, threshold, max_rate):
    pitax=[]
    for income in income:
        if income <= threshold:
            pitax += [0]
        else:
            j = 0
            income = np.arange(threshold, income)
            rate = np.arange(0, max_rate)
            pitax += [income * rate]
    return pitax