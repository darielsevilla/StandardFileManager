from PyQt6.QtWidgets import *
from PyQt6 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("MainFrame.ui", self)
        self.show()