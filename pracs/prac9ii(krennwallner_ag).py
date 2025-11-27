import sys
import os
import pandas as pd
from folium.plugins import FastMarkerCluster, HeatMap
from folium import Marker, Map
import webbrowser

################################################################
# BASE PATH
Base = 'C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs'
print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')
################################################################

# INPUT CSV FILE
sFileName = Base + '/Retrieve_DE_Billboard_Locations.csv'
df = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")
df.fillna(value=0, inplace=True)
print(df.shape)
################################################################

t = 0
for i in range(df.shape[0]):

    try:
        sLongitude = float(df["Longitude"][i])
    except:
        sLongitude = 0.0

    try:
        sLatitude = float(df["Latitude"][i])
    except:
        sLatitude = 0.0

    try:
        sDescription = df["Place_Name"][i] + ' (' + df["Country"][i] + ')'
    except:
        sDescription = 'VKHCG'

    if sLongitude != 0.0 and sLatitude != 0.0:
        DataClusterList = [sLatitude, sLongitude]
        DataPointList = [sLatitude, sLongitude, sDescription]
        t += 1

        if t == 1:
            DataCluster = [DataClusterList]
            DataPoint = [DataPointList]
        else:
            DataCluster.append(DataClusterList)
            DataPoint.append(DataPointList)

data = DataCluster
pins = pd.DataFrame(DataPoint)
pins.columns = ['Latitude', 'Longitude', 'Description']
################################################################

# -----------------------------------------
# MARKER CLUSTER MAP
# -----------------------------------------
stops_map1 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
FastMarkerCluster(data).add_to(stops_map1)

sFileNameHtml = Base + '/Billboard1.html'
stops_map1.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))

################################################################

# -----------------------------------------
# MARKER MAP (FIRST 100 POINTS)
# -----------------------------------------
stops_map2 = Map(location=[48.1459806, 11.4985484], zoom_start=5)

for name, row in pins.iloc[:100].iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup=row["Description"]).add_to(stops_map2)

sFileNameHtml = Base + '/Billboard2.html'
stops_map2.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))

################################################################

# -----------------------------------------
# HEATMAP (FIRST 100 POINTS)
# -----------------------------------------
stops_heatmap = Map(location=[48.1459806, 11.4985484], zoom_start=5)
stops_heatmap.add_child(
    HeatMap([[row["Latitude"], row["Longitude"]] for name, row in pins.iloc[:100].iterrows()])
)

sFileNameHtml = Base + '/Billboard_heatmap.html'
stops_heatmap.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))

################################################################

print('### Done!! ############################################')
