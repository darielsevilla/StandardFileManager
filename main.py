from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import types
from MainFrame import Ui_MainWindow
from VentanaPrincipal import VentanaPrincipal
def main():
    app = QApplication([])
    window = Ui_MainWindow()
    window2 = QMainWindow()
    window.setupUi(window2)

    window2.resize = types.MethodType(newResize, window2)
    window2.show()

    app.exec()

def main2():
    app = QApplication([])
    window = VentanaPrincipal()
    app.exec()
def newResize(self):
    #self.widgetTopMenu_3.setGeometru(0, 0, self.width(),self.height())
    self.repaint()
    print("gay")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
