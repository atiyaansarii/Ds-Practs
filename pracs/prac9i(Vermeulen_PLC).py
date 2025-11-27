import sys
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
################################################################

pd.options.mode.chained_assignment = None
################################################################

# Force Windows base path (your folder)
Base = r"C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs"
################################################################

print('################################')
print('Working Base :', Base, ' using ', sys.platform)
print('################################')
################################################################

sInputFileName = 'Assess-Network-Routing-Customer.csv'
################################################################

sOutputFileName1 = 'Report-Network-Routing-Customer.gml'
sOutputFileName2 = 'Report-Network-Routing-Customer.png'
################################################################

### Import Customer Routing Data
################################################################
sFileName = Base + '/' + sInputFileName
print('################################')
print('Loading :', sFileName)
print('################################')

CustomerDataRaw = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")
CustomerData = CustomerDataRaw.head(100)

print('Loaded Data Columns:', CustomerData.columns.values)
print('################################')
################################################################

print(CustomerData.head())
print(CustomerData.shape)
################################################################

# Build Graph
G = nx.from_pandas_edgelist(CustomerData, "Source", "Target", ["Weight"])

print('Nodes:', G.number_of_nodes())
print('Edges:', G.number_of_edges())
################################################################

# Store GML
sFileName = Base + '/' + sOutputFileName1
print('################################')
print('Storing :', sFileName)
print('################################')
nx.write_gml(G, sFileName)
################################################################

# Store Graph Image
sFileName = Base + '/' + sOutputFileName2
print('################################')
print('Storing Graph Image:', sFileName)
print('################################')

plt.figure(figsize=(25, 25))
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='k', node_size=50, alpha=0.8)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows=False, style='dashed')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_color='b')

plt.axis('off')
plt.savefig(sFileName, dpi=300)
plt.show()
################################################################

print('################################')
print('### Done!! #####################')
print('################################')
