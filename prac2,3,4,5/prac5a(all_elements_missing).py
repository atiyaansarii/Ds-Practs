import sys
import os
import pandas as pd
################################################################
Base = r'C:/Atiya/FY-MSC-IT/Data Science/DS Practs'  # Use raw string for Windows path
################################################################
print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName = 'Good-or-Bad.csv'
sOutputFileName = 'Good-or-Bad-01.csv'
Company = '01-Vermeulen'
################################################################
sFileDir = os.path.join(Base, Company, '02-Assess', '01-EDS', '02-Python')
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName = os.path.join(Base, Company, '00-RawData', sInputFileName)
print('Loading :', sFileName)

if not os.path.isfile(sFileName):
    print("ERROR: File not found:", sFileName)
    exit(1)

RawData = pd.read_csv(sFileName, header=0)
print('################################')
print('## Raw Data Values')
print('################################')
print(RawData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :', RawData.shape[0])
print('Columns :', RawData.shape[1])
print('################################')
################################################################
sFileName = os.path.join(sFileDir, sInputFileName)
RawData.to_csv(sFileName, index=False)
################################################################
TestData = RawData.dropna(axis=1, how='all')
################################################################
print('################################')
print('## Test Data Values')
print('################################')
print(TestData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :', TestData.shape[0])
print('Columns :', TestData.shape[1])
print('################################')
################################################################
sFileName = os.path.join(sFileDir, sOutputFileName)
TestData.to_csv(sFileName, index=False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
################################################################
