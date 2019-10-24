import pandas as pd
import numpy as np

"""
this file is crucial

data5 is the file that goes to R to create the forecast. 
"""

data = pd.read_csv('Lokad_Orders.csv')

data['Quantity'] = data['Quantity'].astype('int')


data['Date'] =pd.to_datetime(data.Date) - pd.to_timedelta(7,unit = 'd')
data =data.groupby(['Id',pd.Grouper(key='Date', freq='W-MON')])['Quantity', 'NetAmount'].sum().reset_index().sort_values('Date')
data.reset_index()

data1 = data.groupby(['Id','Date']).agg({'Quantity': sum}).reset_index()
data['Quantity'] = data['Quantity'].astype('int')
data2 = data.set_index(['Date', 'Id']).Quantity.unstack(-2).\
    reindex(columns=pd.date_range(data['Date'].min(), data['Date'].max(),freq='W-MON'),fill_value=0).\
            stack(dropna=False).unstack().stack(dropna=False).sort_values().reset_index()


data3 = pd.DataFrame(data2)
data3 = data3.sort_values('Id', ascending=True)
data4 = data3.fillna(0)
data4 = data4.rename(columns = {'level_1' : 'Date'})
data4 = data4.rename(columns = {0: 'Quantity'})
data5 = data4.groupby(['Id','Date']).agg({'Quantity': sum})#.reset_index()


Data4 = data5.to_csv('data5.csv')











#Data4 = data5.to_csv('data5.csv')

