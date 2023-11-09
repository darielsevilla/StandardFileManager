from os import listdir
from os.path import isfile, abspath
from PyQt6 import QtWidgets
from PyQt6.QtCore import QFileInfo
from PyQt6.QtGui import QPixmap, QIcon
def listDirectories(path):
    directoryArray = []
    for fpath in listdir(path):
        directoryArray.append(fpath)
    return directoryArray

def changeTextFieldData(comboBox, textfield):
    textfield.setText(abspath(comboBox.currentText()))

#metodos para llenar campos
def setUpDataTypes(comboBox):
    comboBox.addItem("int")
    comboBox.setItemIcon(0, QIcon(QPixmap("images/intIcon.png")))
    comboBox.addItem("char")
    comboBox.setItemIcon(1, QIcon(QPixmap("images/charIcon.png")))
    comboBox.addItem("float")
    comboBox.setItemIcon(2, QIcon(QPixmap("images/floatIcon.png")))

def fillTable(table, file):
    table.setRowCount(0)
    for i in range(file.getCampos().getSize()):

        temporalField = file.getCampo(i)
        table.insertRow(table.rowCount())

        item = QtWidgets.QTableWidgetItem(temporalField.getFieldName())
        item.setFlags(item.flags().ItemIsEditable)
        table.setItem(table.rowCount() - 1, 0, item)

        item = QtWidgets.QTableWidgetItem(temporalField.getDataType())
        item.setFlags(item.flags().ItemIsEditable)
        table.setItem(table.rowCount() - 1, 1, item)

        item = QtWidgets.QTableWidgetItem(str(temporalField.getFieldSize()))
        item.setFlags(item.flags().ItemIsEditable)
        table.setItem(table.rowCount() - 1, 2, item)
def fillComboBoxField(comboBox, file):

    comboBox.clear()

    comboBox.setPlaceholderText("Elija campo")
    comboBox.setCurrentIndex(-1)
    for i in range(file.getCampos().getSize()):
        comboBox.addItem(str(file.getCampo(i)))