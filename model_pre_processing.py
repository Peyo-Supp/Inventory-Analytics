import os
import pandas as pd
import glob
import numpy as np
from ABC_Classifier import df2, what
from inventory_behavior import allez


info = pd.read_csv('Lokad_Item.csv')

s = os.chdir('/Users/pierre/Desktop/Project_inv/output_prediction')


"""this get the output from the forecast and bring it all together in one csv file
R contains the ids
pred95 contains the predictions for each output

newdf is the dataframe that has important (from allez)

from 'allez' dataframe that I used in NewForecast, I multiply each row by 8 so i can attach it with pred95

npw
"""
path = '/Users/pierre/Desktop/Project_inv/output_prediction'
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)

R = pd.DataFrame(np.repeat(df2.values,8, axis=0))

R.columns = df2.columns
R1 = R.sort_values(['Id'], ascending=True).reset_index()

pred95 = concatenated_df['predictions.Hi.95'].values.tolist()
pred95 = pd.DataFrame(pred95)

newdf = pd.DataFrame(np.repeat(allez.values,8, axis=0)).reset_index()
newdf = newdf.rename(columns={0: 'value(in%)', 1: 'Quantity', 2:'Unit_cost', 3:'Category', 4:'SubCategory'})



"""
this creates lists for the 8 periods ahead for each product and it calculates its mean and standard deviation 
"""

df = pd.concat([pred95, newdf,R1], axis=1)
df = df.rename(columns = { 0: 'predictions.Hi.95'})
df1 = df.groupby(['Id']).agg({'predictions.Hi.95': list})

l1 = pd.DataFrame(df1['predictions.Hi.95']).applymap(lambda x: np.mean(x))
l1 = l1.rename(columns={'predictions.Hi.95': 'Predmean'})
l2 = pd.DataFrame(df1['predictions.Hi.95']).applymap(lambda x: np.std(x))
l2 = l2.rename(columns={'predictions.Hi.95': 'Predstd'})

df2 = pd.concat([df1, l1, l2], axis=1)


"""
df2 is the most important dataframe!! before it is ready to go for the replenishment, 
we need to add to it the categories and subcategories.
"""

itemsinfo = pd.DataFrame(info)

lt = pd.DataFrame(itemsinfo['SupplierLeadTime'].astype(int))
df2=df2.reset_index()
df2 = df2.join([lt])

what =what['value(in%)']

"""
now the last step is to reinject the cumulative probabilities so I can classify in classes and append TSL to each 

"""

df2 = df2.join([what])
df2 = df2.sort_values(by='value(in%)', ascending=False)

f = df2['value(in%)'].cumsum()
df2 = df2.merge(f, left_index =True, right_index=True)

classAA = df2[df2['value(in%)_y'] < 40]
classA = df2[(df2['value(in%)_y'] > 40) & (df2['value(in%)_y']<80)]
classB = df2[(df2['value(in%)_y'] > 80) & (df2['value(in%)_y']<90)]
classC = df2[(df2['value(in%)_y'] > 90) & (df2['value(in%)_y'] <99)]
classD = df2[(df2['value(in%)_y'] > 99) & (df2['value(in%)_y'] <102)]


classAA = pd.DataFrame(classAA)
classAA['tsl'] = 0.985
classAA['periods'] =7

classA = pd.DataFrame(classA)
classA['tsl'] = 0.975
classA['periods'] =7

classB = pd.DataFrame(classB)
classB['tsl'] = 0.95
classB['periods'] =7

classC = pd.DataFrame(classC)
classC['tsl'] = 0.93
classC['periods'] =7

classD = pd.DataFrame(classD)
classD['tsl'] =0.90
classD['periods'] =7















#print(final)






