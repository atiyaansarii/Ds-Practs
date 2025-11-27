from matplotlib.pyplot import imread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Input Agreement
sInputFileName = 'C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs\\zebra.jpg'
InputData = imread(sInputFileName)

print('X: ', InputData.shape[0])
print('Y: ', InputData.shape[1])
print('RGBA: ', InputData.shape[2])

# Processing Rules
ProcessRawData = InputData.flatten()
y = InputData.shape[2] + 3
x = int(ProcessRawData.shape[0] / y)
ProcessData = pd.DataFrame(np.reshape(ProcessRawData, (x, y)))

sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue', 'Alpha']
ProcessData.columns = sColumns
ProcessData.index.names = ['ID']

print('Rows: ', ProcessData.shape[0])
print('Columns :', ProcessData.shape[1])

print('Process Data Values ')
plt.imshow(InputData)
plt.show()

# Output Agreement
OutputData = ProcessData
print('Storing File')

sOutputFileName = 'C:\\Atiya\\FY-MSC-IT\\Data Science\\DS Practs\\HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index=False)

print('Picture to HORUS - Done')
