import os
import pandas as pd
import glob
import numpy as np
from ABC_Classifier import df2, what
from inventory_behavior import allez
import operator as op

"""
this file is taking the output of the prediction made with R 
and it combines them into one big dataframe in order to run them through the algorithm

"""

s = os.chdir('/Users/pierre/Desktop/Project_inv/output_prediction')

path = '/Users/pierre/Desktop/Project_inv/output_prediction'
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)

concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)
concatenated_df = concatenated_df['predictions.Hi.95']
#
# concatenated_df = pd.DataFrame(concatenated_df)
#
# R = pd.concat([concatenated_df, df2], axis=1).dropna()

newdf = pd.DataFrame(np.repeat(df2.values,8, axis=0))


newdf.columns = df2.columns
newdf1 = newdf.sort_values(['Id'], ascending=True).reset_index()
print(newdf1)


newdf1 = newdf1['Id']



newdf2 = pd.DataFrame(newdf1)

n = pd.concat([concatenated_df, newdf2, allez], axis=1 )


n['Agg_cost'] = 100
n['holding_rate'] = 0.34
n['init_inventory'] = 0
#n['holding_cost'] = n4['holding_rate']*n4['Unit_cost']


n5 = pd.DataFrame(n['predictions.Hi.95'], n['Id'])




# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#      print(n4)

#n4['predictions.Hi.95'] = pd.DataFrame(n4['predictions.Hi.95']).values
#
# #
# #
# df1 = n4.set_index['Id']
# #result = df1['predictions.Hi.95'].unique()
#
#
# df1 = n4.groupby(['Id']).agg({'predictions.Hi.95': float})
# df2 = n4.groupby(['Id']).agg({'predictions.Hi.95': list, 'Agg_cost' : list, 'holding_rate' : list, 'init_inventory': list, 'holding_cost' : list})
# df2['predictions.Hi.95'] = df2['predictions.Hi.95'].apply(pd.to_numeric)
# df2 = df2.join(allez)
# df2 = df2.sort_values('value(in%)')
#
print(df2['value(in%)'])
# forecastclassAA = df2[(df2['value(in%)'] <= 40)]
# forecastclassA = df2[(df2['value(in%)'] > 40) & (df2['value(in%)']<80)]
#
# #fo = forecastclassA['predictions.Hi.95'].values.tolist().mean()
# #fo =  np.mean(forecastclassA['predictions.Hi.95'].tolist(), axis=1)
# #fo =pd.DataFrame(fo)
# #print(fo)
#
#
# #reduce(lambda x, y : x +y, forecastclassA['predictions.Hi.95'])/forecastclassA['predictions.Hi.95'].len()
# #forecastclassA = forecastclassA.join(fo)
#
#
# forecastclassB = df2[(df2['value(in%)'] > 80) & (df2['value(in%)']<90)]
# forecastclassC = df2[(df2['value(in%)'] > 90) & (df2['value(in%)'] <99)]
# forecastclassD = df2[(df2['value(in%)'] > 99) & (df2['value(in%)'] <102)]
#
#
#
#
# forecastclassAA = pd.DataFrame(forecastclassAA)
#
# print(forecastclassAA)
#
# #forecastclassAA = forecastclassAA.groupby(['Id']).agg({['Unit_cost']: float})
# forecastclassAA = pd.DataFrame(forecastclassAA)
#
#
#
#
#
# #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#
#
# forecastclassA = pd.DataFrame(forecastclassA)
# fca = forecastclassA.groupby(['SubCategory']).agg({'predictions.Hi.95' : list, 'Unit_cost' : list, 'Agg_cost' : list, 'holding_rate': list, 'init_inventory': list, 'holding_cost' : list})
#
#
#
# #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#
#
#
# #print(fca)
#
# forecastclassB = pd.DataFrame(forecastclassB)
# fcb = forecastclassB.groupby(['SubCategory']).agg({'predictions.Hi.95' : list, 'Unit_cost' : list, 'Agg_cost' : list, 'holding_rate': list, 'init_inventory': list, 'holding_cost' : list})
#
# #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     #print(fcb)
# #print(fcb)
#
# forecastclassC = pd.DataFrame(forecastclassC)
# fcc = forecastclassC.groupby(['SubCategory']).agg({'predictions.Hi.95' : list, 'Unit_cost' : list, 'Agg_cost' : list, 'holding_rate' : list, 'init_inventory': list, 'holding_cost' : list})
# #print(fcc)
#
# forecastclassD = pd.DataFrame(forecastclassD)
# fcd = forecastclassA.groupby(['SubCategory']).agg({'predictions.Hi.95' : list, 'Unit_cost' : list, 'Agg_cost' : list, 'holding_rate': list, 'init_inventory': list, 'holding_cost' : list})
# #print(fcd)
#
#
# print(forecastclassAA)
# print(forecastclassA)
# print(forecastclassB)
# print(forecastclassC)
# print(forecastclassD)
#
# #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#      #print(df2)
#
#
# #n5 = n4.set_index('Id')
#
# # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
# #     print(n4)
#
# # nn = pd.DataFrame(n4['Id'])
# # print(nn)
# #n5 = n4.drop(n4.columns[0], axis=1)
#
#
# #
# #
# #
# # n6 = n5.dropna()
# # n6 = n6.join(nn)
# # print(n6)
#
#
#
# #n7 = n6.set_index(['Id']).transpose()
# #print(n1)
# #n4 = n4.drop('index', axis=1)
# #n5 = n4.drop('Id', axis=0)
# #n5 = n5.dropna()
#
# #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#
#
#
#
# # print(df1)
#
# #combined_csv = df1.to_csv('combined_csv.csv')















