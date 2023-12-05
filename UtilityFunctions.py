from os import listdir
from os.path import isfile, abspath
from PyQt6 import QtWidgets
from PyQt6.QtCore import QFileInfo
from PyQt6.QtGui import QPixmap, QIcon
from Archivo import *
from Registro import *
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
    
def fillCityFile(file):
        print("in fillCityFile")
        origin_path = "CityFile.txt"
        with open(origin_path, 'r') as ofile:  
            string = ofile.read()
        cities = string.split('\n')
        #print(cities)
        for city in cities:
            atts = city.split("|")
            atts2 = []
            atts2.append(int(atts[0]))
            atts2.append(str(atts[1]))
            print("currentCity: " , city)
            print("atts2: " , atts2)
            registro = Registro()
            for i in range(len(atts2)):
                print("\n\n in loop\n")
                print(atts2[i])
                registro.addAttribute(atts2[i])
                registro.maxlengths.append(file.getCampo(i).getFieldSize())
                if (file.getCampo(i).isKey() == True):
                    registro.setKey(atts2[i])
                if (file.getCampo(i).getSecondaryKey() == True):
                    registro.setSecKey(atts2[i])
            
            print("regsiterkey", registro.getKey())
            file.writeRegister(registro)

def fillPersonFile(file):
        print("in fillPeopleFile")
        origin_path = "PersonFile.txt"
        with open(origin_path, 'r') as ofile:  
            string = ofile.read()
        people = string.split('\n')
        #print(cities)
        #for person in people:
        try:
            for x in range(10000):
                atts = people[x].split("|")
                atts2 = []
                atts2.append(int(atts[0]))
                name = str(atts[1])
                if(len(name) < 20):
                    atts2.append(name)
                else:
                    atts2.append(name[:20])
                atts2.append(int(atts[2]))
                atts2.append(int(atts[3]))
                print("currentPerson: " , people[x])
                print("atts2: " , atts2)
                registro = Registro()
                for i in range(len(atts2)):
                    print("\n\n in loop\n")
                    print(atts2[i])
                    registro.addAttribute(atts2[i])
                    registro.maxlengths.append(file.getCampo(i).getFieldSize())
                    if (file.getCampo(i).isKey() == True):
                        registro.setKey(atts2[i])
                    if (file.getCampo(i).getSecondaryKey() == True):
                        registro.setSecKey(atts2[i])

                print("regsiterkey", registro.getKey())
                file.writeRegister(registro)
        except Exception as e:
            traceback.print_exc()
            sys.exit()
        print("done")