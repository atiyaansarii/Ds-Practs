import sys
import os
from datetime import datetime
from pytz import timezone
import pandas as pd
import sqlite3 as sq
import uuid

# Disable chained assignment warning in pandas
pd.options.mode.chained_assignment = None

# Set base directories
Base = '/content'
print('Working Base:', Base, 'using', sys.platform)

# File and database setup
InputDir = '/content/'
InputFileName = 'VehicleData.csv'

# Directories for databases
sDataBaseDir = Base + '/DS Assgn/practicals/'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

sDatabaseName = sDataBaseDir + '/Vermeulen.db'
conn1 = sq.connect(sDatabaseName)

sDataVaultDir = Base + '/DS Assgn/practicals/'
if not os.path.exists(sDataVaultDir):
    os.makedirs(sDataVaultDir)

sDatabaseName = sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName)

sDataWarehouseDir = Base + '/DS Assgn/practicals/'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)

sDatabaseName = sDataWarehouseDir + '/datawarehouse.db'
conn3 = sq.connect(sDatabaseName)

# Time Category
print('\n#########')
print('Time Category')
print('UTC Time')

# Birthdate in UTC
BirthDateUTC = datetime(1960, 12, 20, 10, 15, 0)
BirthDateZoneUTC = BirthDateUTC.replace(tzinfo=timezone('UTC'))
BirthDateZoneStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S")
BirthDateZoneUTCStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
print(BirthDateZoneUTCStr)

# Birthdate in Reykjavik time zone
print('#######')
print('Birth Date in Reykjavik:')
BirthZone = 'Atlantic/Reykjavik'
BirthDate = BirthDateZoneUTC.astimezone(timezone(BirthZone))
BirthDateStr = BirthDate.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
BirthDateLocal = BirthDate.strftime("%Y-%m-%d %H:%M:%S")
print(BirthDateStr)

# Generate a unique ID for the zone
IDZoneNumber = str(uuid.uuid4())
sDateTimeKey = BirthDateZoneStr.replace(' ', '-').replace(':', '-')

# TimeLine for UTC birthdate
TimeLine = {
    'ZoneBaseKey': ['UTC'],
    'IDNumber': [IDZoneNumber],
    'DateTimeKey': [sDateTimeKey],
    'UTCDateTimeValue': [BirthDateZoneUTC],
    'Zone': [BirthZone],
    'DateTimeValue': [BirthDateStr]
}
TimeFrame = pd.DataFrame(TimeLine)

# TimeHub creation
TimeHub = TimeFrame[['IDNumber', 'ZoneBaseKey', 'DateTimeKey', 'DateTimeValue']]
TimeHubIndex = TimeHub.set_index(['IDNumber'], inplace=False)

# Storing TimeHub in SQLite
sTable = 'Hub-Time-Gunnarsson'
print('\n#################################')
print('Storing', sDatabaseName, '\n Table:', sTable)
print('#################################')
TimeHubIndex.to_sql(sTable, conn2, if_exists="replace")

# Storing Dim-Time-Gunnarsson table
sTable = 'Dim-Time-Gunnarsson'
TimeHubIndex.to_sql(sTable, conn3, if_exists="replace")

# TimeSatellite creation
TimeSatellite = TimeFrame[['IDNumber', 'DateTimeKey', 'Zone', 'DateTimeValue']]
TimeSatelliteIndex = TimeSatellite.set_index(['IDNumber'], inplace=False)

# Fixing the BirthZone name
BirthZoneFix = BirthZone.replace(' ', '-').replace('/', '-')

# Storing TimeSatellite in SQLite
sTable = 'Satellite-Time-' + BirthZoneFix + '-Gunnarsson'
print('\n#################################')
print('Storing', sDatabaseName, '\n Table:', sTable)
print('#################################')
TimeSatelliteIndex.to_sql(sTable, conn2, if_exists="replace")

# Storing Dim-Time for BirthZone
sTable = 'Dim-Time-' + BirthZoneFix + '-Gunnarsson'
TimeSatelliteIndex.to_sql(sTable, conn3, if_exists="replace")

# Person Category
print('\n#########')
FirstName = 'Guðmundur'
LastName = 'Gunnarsson'
print('Name:', FirstName, LastName)
print('Birth Date:', BirthDateLocal)
print('Birth Zone:', BirthZone)
print('UTC Birth Date:', BirthDateZoneStr)

# Generating a unique ID for the person
IDPersonNumber = str(uuid.uuid4())

# Creating PersonLine for the database
PersonLine = {
    'IDNumber': [IDPersonNumber],
    'FirstName': [FirstName],
    'LastName': [LastName],
    'Zone': ['UTC'],
    'DateTimeValue': [BirthDateZoneStr]
}
PersonFrame = pd.DataFrame(PersonLine)

# TimeHub creation for Person
TimeHub = PersonFrame
TimeHubIndex = TimeHub.set_index(['IDNumber'], inplace=False)

# Storing Person Hub
sTable = 'Hub-Person-Gunnarsson'
print('\n#################################')
print('Storing', sDatabaseName, ' \n Table:', sTable)
print('#################################')
TimeHubIndex.to_sql(sTable, conn2, if_exists="replace")

# Storing Dim-Person-Gunnarsson table
sTable = 'Dim-Person-Gunnarsson'
TimeHubIndex.to_sql(sTable, conn3, if_exists="replace")
