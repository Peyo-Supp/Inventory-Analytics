import pandas as pd
import numpy as np

"""
original dataset:

Id = Item SKU number
Date = date of the purchase
Quantity = quantity of items purchased for each order
Currency = currency used in the transaction
NetAmount = transaction amount 


This code takes a data organized as stated above, and it classifies the sku in 3 classes. 
class A
class B
class C
class D

class A takes the top 60% of the items 
class B takes the remaining 30% of the items
class C takes the remaining items.

It gives out an ABCD matrix with the following information about inventory:

- the class
- the quantity of items in that class
- the percentage that these items represent to the total inventory 
- the cumulative percentage that they to the total inventory 
this program is crucial because it is first step in analyzing the inventory. 

"""


#import the dataset
data= pd.read_csv("Lokad_Orders.csv")
d1= pd.read_csv('Lokad_Items.csv')
#calculate stock value



t = round(data['NetAmount'].sum())
data['Unit_cost']= round(data['NetAmount']/data['Quantity'])

#df2 is the dataframe that has the cost per unit for each sku
dff = pd.DataFrame(data['Unit_cost'])
dff1 = pd.DataFrame(data['Id'])
df2 = pd.concat([dff1,dff], axis=1)
df2.drop_duplicates(subset='Id',keep='first',inplace=True)
df3 = df2.sort_values(by='Id', ascending=True)
df4 = df3.reset_index( drop=True)


#preparer two lists to calculate the quantity of orders of each sku
list2 = data['Id'].values.tolist()
list3 = data['Quantity'].values.tolist()
data = data.values
idcol = data[:,0]
list1 = list(np.unique(idcol))

count = ({i:0 for i in list1})
for i in list2:
    if i in list1:
        count[i] += 1

arr1=np.array(list2)
arr2= np.array(list3) #quantity for each sku
dict={}

for val in arr1:
    list3 = np.nonzero(arr1==val)
    dict[val]=arr2[list3[0]].sum()

for i in sorted (dict.keys()):
    S = i, dict[i]



# #construction of a new dataframe from the two dictionaries
s2= pd. DataFrame.from_dict([dict], orient='columns', dtype=None, columns=None)
s3 = s2.transpose()
s1 = pd.Series(count, index=count.keys())
sr = s2.append(s1, ignore_index=True)
sr1 = sr.transpose()
sr2 = sr1.reset_index(drop=True)

what = pd.concat([sr2,df4],axis = 1, join='outer')
what.columns = ['Quantity','Number_Orders','SKU','Unit_cost']

df = pd.DataFrame(d1).sort_values('Id', ascending=True).dropna(axis= 0).drop(index=118)

what1 = what.join([df['Name'],df['Category'],df['SubCategory']])

what['revenueSKU'] = round(what['Quantity'] * what['Unit_cost'])
what['value(in%)'] = round(((what['revenueSKU']/t)*100),10)

what['revenue%'] = round(what['revenueSKU']/(what['revenueSKU'].sum()), 5).fillna(0)


classifier = pd.concat([what['value(in%)'],what['SKU'], what['revenue%']], axis=1, join='outer')
classifier1 = classifier.sort_values(by='value(in%)',ascending= False)
classifier1 = classifier1.set_index('SKU',drop=True,inplace=False)

cumulative_percentage = classifier1.cumsum()
classAA = cumulative_percentage[cumulative_percentage['value(in%)'] < 40]
classA = cumulative_percentage[(cumulative_percentage['value(in%)'] > 40) & (cumulative_percentage['value(in%)']<80)]
classB = cumulative_percentage[(cumulative_percentage['value(in%)'] > 80) & (cumulative_percentage['value(in%)']<90)]
classC = cumulative_percentage[(cumulative_percentage['value(in%)'] > 90) & (cumulative_percentage['value(in%)'] <99)]
classD = cumulative_percentage[(cumulative_percentage['value(in%)'] > 99) & (cumulative_percentage['value(in%)'] <102)]


classAA = pd.DataFrame(classAA)
AA = classAA.count(axis=0).values
AAMAX = classAA['revenue%'].max()
AAMAX1 = AAMAX


classA = pd.DataFrame(classA)
A = classA.count(axis=0).values
AMAX = classA['revenue%'].max()
AMAX1 = AMAX - AAMAX

classB = pd.DataFrame(classB)
B = classB.count(axis=0).values
BMAX = classB['revenue%'].max()
BMAX1 = BMAX - AMAX

classC = pd.DataFrame(classC)
C = classC.count(axis=0).values
CMAX = classC['revenue%'].max()
CMAX1 = CMAX - BMAX

classD = pd.DataFrame(classD)
D = classD.count(axis=0).values
DMAX = classD['revenue%'].max()
DMAX1 = DMAX - CMAX

PAA = AA/ (AA + A + B + C +D)
PA = A / (AA + A + B + C +D)
PB = B / (AA + A + B + C +D)
PC = C / (AA + A + B + C +D)
PD = D / (AA + A + B + C +D)

#cumul % items "cumul of class AA items percentage
TTT = (AA + A + B + C +D)
PAAP = AA/ (AA + A + B + C +D)
PAP = (AA + A) / (AA + A + B + C +D)
PBP = (AA+A+B)/ (AA + A + B + C +D)
PCP = (AA + A + B + C)/ (AA + A + B + C +D)
PDP = (AA + A + B + C + D) / (AA + A + B + C +D)

#cumul percentage of stock(in units)

#final ABC matrix
class_matrix = pd.DataFrame()
class_matrix['Class'] = ['ClassAA', 'ClassA', 'ClassB', 'ClassC', 'ClassD']
class_matrix['Quantity-Items'] = [AA, A, B, C, D]
class_matrix['%of_total_stock'] = [PAA, PA, PB, PC, PD]
class_matrix['cumul%_total'] = [PAAP, PAP, PBP, PCP, PDP]
class_matrix['$of_total'] = [AAMAX1, AMAX1, BMAX1, CMAX1, DMAX1]
class_matrix['%cumul_total_revenue'] = [AAMAX, AMAX, BMAX, CMAX, DMAX]

class_matrix.to_excel("NEWInventory_class_matrix.xlsx")

