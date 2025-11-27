################################################################
# -*- coding: utf-8 -*-
################################################################

import sys
import os
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

################################################################
# Set base folder
################################################################

Base = r"C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs\\prac6"

print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')

################################################################

Company = '01-Vermeulen'
EDSAssessDir = '02-Assess/01-EDS'
InputAssessDir = EDSAssessDir + '/02-Python'

################################################################
# Directory creation
################################################################

sFileAssessDir = os.path.join(Base, Company, InputAssessDir)
os.makedirs(sFileAssessDir, exist_ok=True)

sDataBaseDir = os.path.join(Base, Company, '03-Process/SQLite')
os.makedirs(sDataBaseDir, exist_ok=True)

sDataVaultDir = os.path.join(Base, '88-DV')
os.makedirs(sDataVaultDir, exist_ok=True)

################################################################
# SQLite connections
################################################################

ProcessDB = os.path.join(sDataBaseDir, 'Vermeulen.db')
DataVaultDB = os.path.join(sDataVaultDir, 'datavault.db')

conn1 = sq.connect(ProcessDB)
conn2 = sq.connect(DataVaultDB)

################################################################
# Create location grid
################################################################

t = 0
tMax = 360 * 180

rows = []   # MUCH faster than append()

for Longitude in range(-180, 180, 10):
    for Latitude in range(-90, 90, 10):
        t += 1
        IDNumber = str(uuid.uuid4())
        LocationName = f"L{Longitude*1000:+07.0f}-{Latitude*1000:+07.0f}"

        print(f"Create: {t} of {tMax}: {LocationName}")

        rows.append({
            'ObjectBaseKey': 'GPS',
            'IDNumber': IDNumber,
            'LocationNumber': t,
            'LocationName': LocationName,
            'Longitude': Longitude,
            'Latitude': Latitude
        })

################################################################
# Create DataFrame
################################################################

LocationFrame = pd.DataFrame(rows)
LocationHubIndex = LocationFrame.set_index('IDNumber')

################################################################
# Store in Process database
################################################################

sTable = 'Process-Location'
print("Storing:", ProcessDB, "Table:", sTable)
LocationHubIndex.to_sql(sTable, conn1, if_exists="replace")

################################################################
# Store in DataVault database
################################################################

sTable = 'Hub-Location'
print("Storing:", DataVaultDB, "Table:", sTable)
LocationHubIndex.to_sql(sTable, conn2, if_exists="replace")

################################################################
# Vacuum databases
################################################################

print("################")
print("Vacuum Databases")

sql.execute("VACUUM;", conn1)
sql.execute("VACUUM;", conn2)

################################################################
print("### Done!! ############################################")
################################################################
