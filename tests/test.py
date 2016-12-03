# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QItemSelectionModel")
window.resize(300, 400)
tableView = QtGui.QTableView()
listView = QtGui.QListView()

model = QtGui.QStandardItemModel(3, 1)
for row in range(0, 3):
    item = QtGui.QStandardItem("Пункт {0}".format(row))
    model.setItem(row, 0, item)
model.setHorizontalHeaderLabels(["A"])
model.setVerticalHeaderLabels(["01", "02", "03"])

selModel = QtGui.QItemSelectionModel(model)

tableView.setModel(model)
listView.setModel(model)

tableView.setSelectionModel(selModel)
listView.setSelectionModel(selModel)

box = QtGui.QVBoxLayout()
box.addWidget(tableView)
box.addWidget(listView)
window.setLayout(box)
window.show()
sys.exit(app.exec_())
