################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

pd.options.mode.chained_assignment = None

################################################################
# FIXED BASE PATH (YOUR PATH)
################################################################
Base = r'C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs\\prac6'

print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')

################################################################
Company = '03-Hillman'
InputDir = '00-RawData'
InputFileName = 'VehicleData.csv'

################################################################
# Create SQLite Directory
################################################################
sDataBaseDir = Base + '/' + Company + '/03-Process/SQLite'
os.makedirs(sDataBaseDir, exist_ok=True)

# Database file
sDatabaseName = sDataBaseDir + '/Hillman.db'
conn = sq.connect(sDatabaseName)

################################################################
# Load CSV
################################################################
sFileName = Base + '/' + Company + '/' + InputDir + '/' + InputFileName

print('###########')
print('Loading :', sFileName)
VehicleRaw = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")

################################################################
# Store Raw Data
################################################################
sTable = 'Raw_VehicleData'
print('Storing :', sDatabaseName, ' Table:', sTable)
VehicleRaw.to_sql(sTable, conn, if_exists="replace", index=False)

################################################################
# Create Keys
################################################################
VehicleKey = VehicleRaw[['VehicleMake', 'VehicleModel']].drop_duplicates()

VehicleKey['ObjectKey'] = VehicleKey.apply(
    lambda row: f"({str(row['VehicleMake']).strip().lower().replace(' ', '-')})-({str(row['VehicleModel']).strip().lower().replace(' ', '-')})",
    axis=1
)

VehicleKey['ObjectType'] = 'vehicle'
VehicleKey['ObjectUUID'] = VehicleKey.apply(lambda x: str(uuid.uuid4()), axis=1)

################################################################
# Hub Table
################################################################
Hub_Vehicle = VehicleKey[['ObjectType', 'ObjectKey', 'ObjectUUID']].copy()
Hub_Vehicle.index.name = 'HubID'

print("Storing Hub_Vehicle...")
Hub_Vehicle.to_sql("Hub_Vehicle", conn, if_exists="replace")

################################################################
# Satellite Table
################################################################
Sat_VehicleDetails = VehicleKey[['ObjectUUID', 'VehicleMake', 'VehicleModel']].copy()
Sat_VehicleDetails.index.name = "SatID"

print("Storing Sat_VehicleDetails...")
Sat_VehicleDetails.to_sql("Sat_VehicleDetails", conn, if_exists="replace")

################################################################
# Dimension View
################################################################
print("Creating View: Dim_Vehicle")

sSQL = """
CREATE VIEW IF NOT EXISTS Dim_Vehicle AS
SELECT 
    H.ObjectType,
    H.ObjectKey AS VehicleKey,
    S.VehicleMake,
    S.VehicleModel
FROM Hub_Vehicle H
JOIN Sat_VehicleDetails S
ON H.ObjectUUID = S.ObjectUUID;
"""
sql.execute(sSQL, conn)

################################################################
# Load Dimension View
################################################################
print("Loading Dim_Vehicle...")

sSQL = """
SELECT DISTINCT VehicleMake, VehicleModel
FROM Dim_Vehicle
ORDER BY VehicleMake, VehicleModel;
"""

DimObjectData = pd.read_sql_query(sSQL, conn)
DimObjectData.index.name = 'ObjectDimID'

print(DimObjectData)

################################################################
# Vacuum Database
################################################################
print("################")
print("Vacuum Databases")

sql.execute("VACUUM;", conn)

################################################################
conn.close()
print("### Done!! ############################################")
################################################################
