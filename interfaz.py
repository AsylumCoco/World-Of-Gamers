import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem
import pandas as pd

archivo = "G:\Python\pruebas\productos.xlsx"
productos = pd.read_excel(archivo)
print(str(len(archivo.columns)))
#print(productos)

'''
app = QApplication(sys.argv)

window = QMainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
win = QWidget()
scroll = QScrollArea()
layout = QVBoxLayout()
table = QTableWidget()
scroll.setWidget(table)
layout.addWidget(table)
win.setLayout(layout)    

table.setColumnCount(len(archivo.columns))
table.setRowCount(len(archivo.index))
for i in range(len(archivo.index)):
	for j in range(len(archivo.columns)):
		table.setItem(i, j, QTableWidgetItem(str(archivo.iloc[i, j])))

win.show()
app.exec_()
'''