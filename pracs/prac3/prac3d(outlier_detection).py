import pandas as pd

InputFileName = 'IP_DATA_CORE.txt'
OutputFileName = 'Retrieve_Router_Location.csv'
Base = 'C:/Atiya/FY-MSC-IT/Data Science/DS Practs'

print('Working Base :', Base)

sFileName = Base + '/' + InputFileName
print('Loading :', sFileName)

IP_DATA_ALL = pd.read_csv(
    sFileName,
    header=0,
    low_memory=False,
    usecols=['Country', 'Latitude', 'Place Name', 'Longitude'],
    encoding="latin-1"
)

IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)

LondonData = IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name'] == 'London']

AllData = LondonData[['Country', 'Place_Name', 'Latitude']]

print('All Data')
print(AllData)
