import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ABC_Classifier import TTT
"""
this file is providing visualization to better understand the behavior of the inventory overtime. 

first visual: bar graph about the movement of inventory
second visual visualization of the evolution of the weekly demand for the overall inventory

and then the last set of visual shows the evolution of the inventory each year
"""
data= pd.read_csv("Lokad_Orders.csv")

"""
the following code is used to model the behavior of the inventory in terms of selling pace
"""


data['Date'] =pd.to_datetime(data.Date) - pd.to_timedelta(7,unit = 'd')
data = data.groupby(['Id',pd.Grouper(key='Date', freq='W-MON')])['Quantity'].sum().reset_index().sort_values('Date')
data = data.reset_index()

data1 = data.groupby(['Id']).agg({'Quantity': sum, 'Date': list}).reset_index()
data1['totalDweek']= data1['Date'].str.len()

#SSM = Super_slow_movers represent less than 1/10 of the mean of the pace of the total inventory
SSM = data1[data1['totalDweek'] < data1['totalDweek'].mean()/10]
SSM1 = float(SSM['totalDweek'].count()/TTT)

#slow movers, between mean/10 and mean/1.3
SM = data1[(data1['totalDweek'] >= data1['totalDweek'].mean()/10) & (data1['totalDweek'] < data1['totalDweek'].mean()/1.3)]
SM1 = float(SM['totalDweek'].count()/TTT)

#regular movers between mean/1.3 and mean*1.1 (should be the biggest chunk
RM = data1[(data1['totalDweek'] >= data1['totalDweek'].mean()/1.3) & (data1['totalDweek'] < data1['totalDweek'].mean()*1.1)]
RM1 = float(RM['totalDweek'].count()/TTT)

#fairly fast movers between mean*1.1 and mean*1.65
FFM = data1[(data1['totalDweek'] >= data1['totalDweek'].mean()*1.1) & (data1['totalDweek'] < data1['totalDweek'].mean()*1.65)]
FFM1 = float(FFM['totalDweek'].count()/TTT)

#fast movers more than mean*1.65
FM = data1[(data1['totalDweek'] >= data1['totalDweek'].mean()*1.65)]
FM1 = float(FM['totalDweek'].count()/TTT)

objectx = ['<0.1', '0.1-0.75', '0.75-1.1', '1.1-1.65', '>1.65']
x_pos = np.arange(len(objectx))

objecty =['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']
y_pos = np.arange(len(objecty))
percentages = [SSM1, SM1, RM1, FFM1, FM1]

plt.bar(x_pos, percentages, align ='center', alpha=0.5)
plt.xticks(x_pos,objectx)
plt.yticks(y_pos, objecty)
plt.ylabel('%ofSKU')
plt.title('units/week')
plt.show()


"""
the following code is plotting the demand for all the item
the first plot show the demand for the entire dataset 

A plot is created for each year of demand

"""

#here is for the visualization# #evolution of the weekly demand for the overall inventory
data1 = data.groupby(['Date']).agg({'Quantity': sum}).reset_index()
data1.set_index(['Date'],inplace=True)
plt.plot(data1.index,data1.Quantity)
plt.show()

data['Date'] =pd.to_datetime(data.Date) - pd.to_timedelta(7,unit = 'd')
data =data.groupby(['Id',pd.Grouper(key='Date', freq='W-MON')])['Quantity'].sum().reset_index().sort_values('Date')
data1.reset_index()

#years is a list of dataframes from the split
years = np.array_split(data1, len(data1.index)/52)

for i in years:
    plt.plot(i.index, i.Quantity)
    plt.ylabel('Total Demand')
    plt.title('evolutions of total demand per week for 1 year')
    plt.show()









