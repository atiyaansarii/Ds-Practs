# #Utility Start Database to HORUS 
import pandas as pd
import sqlite3 as sq

# Input Agreement
sInputFileName = 'C:/Atiya/FY-MSC-IT/Data Science/DS Practs/prac2d/utility.db'
sInputTable = 'Country_Code'
conn = sq.connect(sInputFileName)

sSQL = 'select * FROM ' + sInputTable + ';'
InputData = pd.read_sql_query(sSQL, conn)

print('Input Data Values')
print(InputData)
print("Actual Columns:", InputData.columns)

# Processing Rules
ProcessData = InputData

# Remove columns (corrected names)
ProcessData.drop('ISO_2_CODE', axis=1, inplace=True)
ProcessData.drop('ISO_3_Code', axis=1, inplace=True)

# Rename Country and ISO-M49 (corrected name)
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO_M49': 'CountryNumber'}, inplace=True)

# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)

# Sort data by CountryName
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print('Process Data Values ')
print(ProcessData)

# Output Agreement 
OutputData = ProcessData
sOutputFileName = 'C:/Atiya/FY-MSC-IT/Data Science/DS Practs/prac2d/DATABASE-HORUS-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)

print('Database to HORUS - Done')
