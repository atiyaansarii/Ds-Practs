import pandas as pd
import sqlite3
import os

################################################################
### BASE PATH (as requested)
################################################################
base_path = r"C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs\\prac6"

# Your input CSV file for RawData
input_csv = os.path.join(base_path, "VKHCG_Shares.csv")   # <-- Change filename if needed

################################################################
### Load RawData (THIS FIXES YOUR ERROR)
################################################################
RawData = pd.read_csv(input_csv)

################################################################
### Create folders to store CSV output
################################################################
sFileDir1 = os.path.join(base_path, "Retrieve")
sFileDir2 = os.path.join(base_path, "Assess")
sFileDir3 = os.path.join(base_path, "Process")

os.makedirs(sFileDir1, exist_ok=True)
os.makedirs(sFileDir2, exist_ok=True)
os.makedirs(sFileDir3, exist_ok=True)

################################################################
### Create SQLite DB connection
################################################################
sDatabaseName = os.path.join(base_path, "SharesDB.db")
conn = sqlite3.connect(sDatabaseName)

################################################################
### Import Shares Data Details
################################################################

nShares = RawData.shape[0]

for sShare in range(nShares):

    sShareName = str(RawData['Shares'][sShare])

    # ----------------------------------------------
    #  Replace Quandl with dummy offline stock data
    # ----------------------------------------------
    print("Using offline dummy share data instead of Quandl:", sShareName)

    dates = pd.date_range(start="2023-01-01", periods=30, freq='D')
    ShareData = pd.DataFrame({
        "Date": dates,
        "Open": 100,
        "High": 105,
        "Low": 95,
        "Close": 102,
        "Volume": 100000,
    })

    UnitsOwn = RawData['Units'][sShare]

    ShareData['UnitsOwn'] = UnitsOwn
    ShareData['ShareCode'] = sShareName

    print('################')
    print('Share :', sShareName)
    print('Rows\t:', ShareData.shape[0])
    print('Columns:', ShareData.shape[1])
    print('################')

    ###############################################################

    print('################')
    sTable = str(RawData['sTable'][sShare])
    print('Storing :', sDatabaseName, ' Table:', sTable)
    ShareData.to_sql(sTable, conn, if_exists="replace", index=False)
    print('################')

    ###############################################################

    sOutputFileName = sTable.replace("/", "-") + ".csv"

    # Retrieve files
    file1 = os.path.join(sFileDir1, "Retrieve_" + sOutputFileName)
    ShareData.to_csv(file1, index=False)

    # Assess files
    file2 = os.path.join(sFileDir2, "Assess_" + sOutputFileName)
    ShareData.to_csv(file2, index=False)

    # Process files
    file3 = os.path.join(sFileDir3, "Process_" + sOutputFileName)
    ShareData.to_csv(file3, index=False)

print("### Done!! ############################################")
