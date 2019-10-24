import pandas as pd
import numpy as np
from model_pre_processing import classAA, classA, classB, classC, classD
from scipy.stats import norm
import math as m


"""
this calculate the Re-order point and the safety stock type 1  necessary for each item.


"""

# classAA['SupplierLeadTime'] = classAA['SupplierLeadTime'].astype(float)
classAA['ss'] = norm.ppf(classAA['tsl'])*classAA['Predstd']*np.sqrt((classAA['SupplierLeadTime']/classAA['periods']))
classAA['ROP'] = classAA['SupplierLeadTime']/classAA['periods']*classAA['Predmean'] + classAA['ss']

classA['ss'] = norm.ppf(classA['tsl'])*classA['Predstd']*np.sqrt((classA['SupplierLeadTime']/classA['periods']))
classA['ROP'] = classA['SupplierLeadTime']/classA['periods']*classA['Predmean'] + classA['ss']

classB['ss'] = norm.ppf(classB['tsl'])*classB['Predstd']*np.sqrt((classB['SupplierLeadTime']/classB['periods']))
classB['ROP'] = classB['SupplierLeadTime']/classB['periods']*classB['Predmean'] + classB['ss']

classC['ss'] = norm.ppf(classC['tsl'])*classC['Predstd']*np.sqrt((classC['SupplierLeadTime']/classC['periods']))
classC['ROP'] = classC['SupplierLeadTime']/classC['periods']*classC['Predmean'] + classC['ss']

classD['ss'] = norm.ppf(classD['tsl'])*classD['Predstd']*np.sqrt((classD['SupplierLeadTime']/classD['periods']))
classD['ROP'] = classD['SupplierLeadTime']/classD['periods']*classD['Predmean'] + classD['ss']




