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
    string = abspath(comboBox.currentText())
    string = string.replace(comboBox.currentText(), "registros\\"+ comboBox.currentText())
    textfield.setText(string)

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

def fillCombinedComboBox(comboBox, file, file2):
    comboBox.clear()
    comboBox.setPlaceholderText("Elija campo")
    comboBox.setCurrentIndex(-1)

    for i in range(file.getCampos().getSize()):
        isCombined = False
        campoActual = file.getCampo(i)
        for j in range(file2.getCampos().getSize()):
            campo2 = file2.getCampo(j)

            if campoActual.getFieldName() == campo2.getFieldName() and campoActual.getFieldSize() == campo2.getFieldSize() and campoActual.getDataType() == campo2.getDataType():
                if(campo2.isKey() == True):
                    isCombined = True

        if isCombined == True:
            comboBox.addItem(file.getCampo(i).getFieldName())

def addElementToList(comboBox, list):
    if comboBox.currentIndex() != -1:
        text = comboBox.currentText()
        alreadyThere = False
        for i in range(list.count()):
            if list.item(i).text() == text:
                alreadyThere = True

        if alreadyThere is False:
            item = QtWidgets.QListWidgetItem(text)
            list.addItem(item)

def fillComboBoxIndex(comboBox, file):
    comboBox.clear()
    comboBox.setPlaceholderText("Elija campo para indexar")
    comboBox.setCurrentIndex(-1)
    for i in range(file.getCampos().getSize()):
        campo = file.getCampo(i)
        if campo.isKey() == False and campo.getSecondaryKey() == False:
            comboBox.addItem(campo.getFieldName())

def fillComboBoxReIndex(comboBox, file):
    comboBox.clear()
    comboBox.setPlaceholderText("Elija campo para indexar")
    comboBox.setCurrentIndex(-1)
    for i in range(file.getCampos().getSize()):
        campo = file.getCampo(i)
        if campo.getSecondaryKey() == True:
            comboBox.addItem(campo.getFieldName())

def fillComboBoxKeys(comboBox, file):
    comboBox.clear()
    for i in range(file.getCampos().getSize()):
        campo = file.getCampo(i)
        if campo.getSecondaryKey() or campo.isKey():
            comboBox.addItem(campo.getFieldName())