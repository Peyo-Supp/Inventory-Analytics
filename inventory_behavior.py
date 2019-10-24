import numpy as np
import pandas as pd
from classifier2 import what1, what
import matplotlib.pyplot as plt


"""
dataframe that provides very good info about individual classes!

"""
#v = what['value(in%)'].cumsum()
what2 = what1.join(what['value(in%)'])

what3 = what2.sort_values(by='value(in%)',ascending= False)
what4 = what3.set_index('SKU',drop=True,inplace=False)
what5 = pd.DataFrame(what4)
what6 = pd.concat([what5['value(in%)']]).cumsum()   #.join(what5['Name'], what5['Quantity'], what5['Unit_cost'])
what7 = pd.concat([what6, what5['Quantity'], what5['Unit_cost'], what5['Category'], what5['SubCategory']], axis=1)

#print(what7)
classAA = what7[(what7['value(in%)'] <= 40)]
classA = what7[(what7['value(in%)'] > 40) & (what7['value(in%)']<80)]
classB = what7[(what7['value(in%)'] > 80) & (what7['value(in%)']<90)]
classC = what7[(what7['value(in%)'] > 90) & (what7['value(in%)'] <99)]
classD = what7[(what7['value(in%)'] > 99) & (what7['value(in%)'] <102)]



classAA = pd.DataFrame(classAA)
classA = pd.DataFrame(classA)
classB = pd.DataFrame(classB)
classC = pd.DataFrame(classC)
classD = pd.DataFrame(classD)


allez = pd.concat([classAA, classA, classB, classC, classD])
allez = allez.sort_values('SKU', ascending=True)



