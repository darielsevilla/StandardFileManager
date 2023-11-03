from os import listdir
from os.path import isfile, abspath
from PyQt6 import QtWidgets
from PyQt6.QtCore import QFileInfo
def listDirectories(path):
    directoryArray = []
    for fpath in listdir(path):
        directoryArray.append(fpath)
    return directoryArray

def changeTextFieldData(comboBox, textfield):
    textfield.setText(abspath(comboBox.currentText()))