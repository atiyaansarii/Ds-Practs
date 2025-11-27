import pandas as pd

# Input Agreement
sInputFileName = 'C:/Atiya/FY-MSC-IT/Data Science/DS Practs/Country_Code.txt'
InputData = pd.read_csv(sInputFileName, encoding="latin-1", sep="\t")
print('Input Data Values')
print(InputData)

# Processing Rules
ProcessData = InputData

# Remove columns ISO-2 and ISO-3 (correct names)
ProcessData.drop('ISO-2', axis=1, inplace=True)
ProcessData.drop('ISO-3', axis=1, inplace=True)

# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)

# Sort data by CountryName
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print('Process Data Values ')
print(ProcessData)

OutputData = ProcessData
sOutputFileName = "C:/Atiya/FY-MSC-IT/Data Science/DS Practs/Country_Code.csv"
OutputData.to_csv(sOutputFileName, index=False)

print('CSV to HORUS - Done')
print("MSC IT")
