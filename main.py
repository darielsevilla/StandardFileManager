import sys
import threading
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import types
from MainFrame import Ui_MainWindow
from VentanaPrincipal import VentanaPrincipal
from PyQt6.QtGui import QPixmap, QIcon



def main():

    app = QApplication([])
    window = Ui_MainWindow()
    window2 = QMainWindow()
    window.setupUi(window2)


    window2.show()

    app.exec()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.setrecursionlimit(300000)
    threading.stack_size(9999999)
    mainThread = threading.Thread(target=main)
    mainThread.run()
    #main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
