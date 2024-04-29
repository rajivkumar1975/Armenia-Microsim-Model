# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 06:54:15 2024

@author: wb395723
"""

import pandas as pd
import numpy as np
import json


# df = pd.read_csv("C:/Users/wb395723/OneDrive - WBG/Tax Microsim Model/New_Training_Tax_Microsimulation/tot_revenue_projection.csv", index_col=0)

# df = df.T

# df1=df[df.columns[:2]]
# df1.columns=['Current Law', 'Reform']

# with open('current_law_policy_cit_armenia.json') as f:
#     input_json = json.load(f)

# input_json = dict(sorted(input_json.items()))
# for k, v in input_json.items():
#     for s, m in v.items():
#         if s == "long_name":
#             print(m)

df = pd.read_csv("C:/Users/wb395723/OneDrive - WBG/Tax Microsim Model/New_Training_Tax_Microsimulation/taxcalc/cit_data_armenia.csv")

    
#data = pd.read_csv("C:/Users/wb395723/OneDrive - WBG/Tax Microsim Model/New_Training_Tax_Microsimulation/taxcalc/cit_data_armenia.csv")

# revenue_dict = {}
# with open("C:/Users/wb395723/OneDrive - WBG/Tax Microsim Model/New_Training_Tax_Microsimulation/revenue_dict.json", 'w') as f:
#     json.dump(revenue_dict, f)

# tax_list = ['cit', 'tot']
# for tax_type in tax_list:
#     for k, v in revenue_dict[tax_type].items():
#         print(k, v)
            # revenue_dict_df[k] = {}
            # for k1 in revenue_dict[tax_type][year]['current_law']['value'].keys():
            #     revenue_dict_df[k]['current_law_'+k1] = revenue_dict[tax_type][k]['current_law']['value_bill_str'][k1]
            #     revenue_dict_df[k]['reform_'+k1] = revenue_dict[tax_type][k]['reform']['value_bill_str'][k1]
            #     if adjust_behavior:
            #         revenue_dict_df[k]['reform_behavior_'+k1] = revenue_dict[tax_type][k]['reform_behavior']['value_bill_str'][k1]



# #cols = data.select_dtypes(include=['float64', 'int64']).columns
# cols = ['o_pay_150_percent_base', 'Op_WDV_prop', 'Op_WDV_intang', 'Op_und_amt', 'Loss_lag1', 'Loss_lag2', 
#         'Loss_lag3', 'Loss_lag4', 'Loss_lag5', 'Loss_lag6', 'Loss_lag7', 'Loss_lag8', 'Loss_lag9', 'Loss_lag10']
# for col in cols:
#     #data[col] = data[col].abs().astype('float64')
#     data[col] = data[col].astype('float64')
# col_list = []

# for col in data.columns:
#     if col[:3] == 'exp' or col[:5] == 'o_pay' or col[:3] == 'ded' or col[:4] == 'loss':
#         col_list+=[col]
# for col in col_list:
#     data[col] = data[col].abs()

# data['incentives_tax_reduction'] = data['incentives_tax_reduction'].abs()
# data['profit_tax_reduction_citizens'] = data['profit_tax_reduction_citizens'].abs()
# data['profit_tax_reduction_projects'] = data['profit_tax_reduction_projects'].abs()
    
#data['exp_supplied_goods'] = data['exp_supplied_goods'].abs()
# data['o_pay_150_percent_base'] = data.o_pay_150_percent/1.5

# data['Op_WDV_prop'] = data.ab_tx_prop_jan1
# data['Op_WDV_intang'] = data.ab_tx_int_assets_jan1
# data['Op_und_amt'] = data.unded_trans_tax_prev_q

# for i in range(1, 11):
#     data['Loss_lag' + str(i)] = 0.0

# cols1 = ['DataSet', 'id_n', 'Year', 'sector', 'sector_short', 'sec_desc', 'region']

# cols_int = ['DataSet', 'id_n', 'Year']

# for a in cols_int:
#     data[a] = data[a].astype('int64')

# cols2 = list([a for a in data.columns if a not in cols1])

# data = data.reindex(columns=(cols1 + cols2))

# data.to_csv('cit_data_armenia.csv', index=False)