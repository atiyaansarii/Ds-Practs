import sys
import os
import pandas as pd
pd.options.mode.chained_assignment = None

# Set Base folder to your path - use raw string or forward slashes
Base = r'C:/Atiya/FY-MSC-IT/Data Science/DS Practs'

print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')

sInputFileName = Base + r'\01-Vermeulen\02-Assess\01-EDS\02-Python\Assess-NetworkRouting-Customer.csv'
sOutputFileName = 'Assess-Network-Routing-Customer.gml'
Company = '01-Vermeulen'

sFileName = sInputFileName

print('################################')
print('Loading :', sFileName)
print('################################')

CustomerData = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin1")

print('Loaded Columns:', CustomerData.columns.values)
print('################################')
print(CustomerData.head())
print('################################')
print('### Done!! #####################')
print('################################')
