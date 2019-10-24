import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from forecast import

data = pd.read_csv('Lokad_PurchaseOrders1.csv')


#average order quantity per item
data1 = data.groupby('Id')['Quantity'].agg(['mean','count']).reset_index()
data2 = data.groupby('Id')['NetAmount'].agg(['mean','count']).reset_index()

classifier = pd.concat([data1, data2], axis=1, join= 'outer')
classifier.columns = ['SKU','mean_order_quantity','Number_order','Id','mean_order_price', 'count']

classifier1 = pd.DataFrame([classifier['SKU'],classifier['mean_order_quantity'], classifier['Number_order'],classifier['mean_order_price']])
classifier2 = classifier1.transpose()

t = classifier2['Number_order'].sum()
classifier2['%oftotalorders'] = round((classifier2['mean_order_quantity']/t*100),10)













