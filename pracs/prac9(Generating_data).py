import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import PieChart3D, Reference

# Create a new workbook and worksheet
wb_pie_chart = Workbook()
ws_pie_chart = wb_pie_chart.active

# Data to be added to the worksheet
data = [
    ("Type of Expense", "Amount Spent"),
    ("Grocery", 300),
    ("Electricity", 150),
    ("Child Tuition", 125),
    ("House Keeping", 35),
    ("Gardening", 30),
    ("Misl. Expense", 500),
]

# Append data to the worksheet
for row in data:
    ws_pie_chart.append(row)

# Create a 3D Pie Chart
pie = PieChart3D()

# Set labels and data for the chart
labels = Reference(ws_pie_chart, min_col=1, min_row=2, max_row=7)
data = Reference(ws_pie_chart, min_col=2, min_row=1, max_row=7)

# Add data and labels to the chart
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)

# Add title to the chart
pie.title = "Expenditures Pie Chart"

# Add the chart to the worksheet
ws_pie_chart.add_chart(pie, "C10")

# Save the workbook (use a path suitable for Colab)
wb_pie_chart.save(r"C:\Users\IT-SECTION\Desktop\DS Pract 6-9\pie_chart.xlsx")
print("Data saved to '/content/pie_chart.xlsx'")
