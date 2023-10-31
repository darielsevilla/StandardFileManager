from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon, QPalette, QColor
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        #variables importantes
        self.topMenuQw = QWidget()
        self.sideMenu1Qw = QWidget()

        self.btnArchivo = QPushButton()
        self.btnCampo = QPushButton()
        self.btnRegistro = QPushButton()
        self.btnIndice = QPushButton()
        self.btnEstandarizacion = QPushButton()

        self.opcionesArchivo = []
        #creacion de ventana
        self.buildingWindow()
        self.show()



    def buildingWindow(self):
        #minimum size
        self.setMinimumSize(800, 600)
        layout = self.layout()
        #extras
        lineaNegra = QLine()
        lineaNegra.setLine(0, self.height()/6, self.width(), self.height()/6)

        #panel central
        centralQw = QWidget()
        paletteCentral = centralQw.palette()
        paletteCentral.setColor(centralQw.backgroundRole(), QColor(43, 43, 43))
        centralQw.setAutoFillBackground(True)
        centralQw.setPalette(paletteCentral)
        self.setCentralWidget(centralQw)

        #top menu
        palleteMenus = self.topMenuQw.palette()
        palleteMenus.setColor(self.topMenuQw.backgroundRole(), QColor(60, 63, 65))
        self.topMenuQw.setPalette(palleteMenus)
        layout.addWidget(self.topMenuQw)

        #side menu
        palleteSideButtons = QPalette();
        #menu archivos
        layoutFiles = QVBoxLayout()
        self.sideMenu1Qw.setPalette(palleteMenus)

        textoNecesario = ["Nuevo Archivo", "Abrir Archivo", "Salvar Archivo", "Cerrar Archivo", "Salir"]

        for i in range(5):
            self.opcionesArchivo.append(QWidget())
            label = QLabel(self.opcionesArchivo[i])
            self.opcionesArchivo[i].setAutoFillBackground(True)
            palleteSideButtons.setColor(self.opcionesArchivo[i].backgroundRole(), QColor(217,217,214))
            self.opcionesArchivo[i].setPalette(palleteSideButtons)
            self.opcionesArchivo[i].setMaximumHeight(self.opcionesArchivo[i],100)

            label.setText(textoNecesario[i])

            layoutFiles.addWidget(self.opcionesArchivo[i])




        layout.addWidget(self.sideMenu1Qw)
        self.sideMenu1Qw.setLayout(layoutFiles)


        #buttons (top menu)
        self.btnArchivo.setText("Archivos")
        layout.addWidget(self.btnArchivo)
        self.btnCampo.setText("Campos")
        layout.addWidget(self.btnCampo)
        self.btnRegistro.setText("Registros")
        layout.addWidget(self.btnRegistro)
        self.btnIndice.setText("Indice")
        layout.addWidget(self.btnIndice)
        self.btnEstandarizacion.setText("Estandarizacion")
        layout.addWidget(self.btnEstandarizacion)





    def resizeEvent(self, event):
        #top menu
        self.topMenuQw.setGeometry(0, 0, self.width(), self.height()/6)
        self.topMenuQw.setAutoFillBackground(True)

        #side menu
        self.sideMenu1Qw.setGeometry(0, self.height() / 6, self.width() / 6, self.height())
        self.sideMenu1Qw.setAutoFillBackground(True)

        #buttons (top menu)
        self.btnArchivo.setGeometry((self.centralWidget().width() / 6) + 10, 10, (self.centralWidget().width() * (1 / 6)) - 20,self.topMenuQw.height() - 20)
        self.btnCampo.setGeometry((self.centralWidget().width() *(2/ 6)) + 10, 10, (self.centralWidget().width() * (1 / 6)) - 20, self.topMenuQw.height() - 20)
        self.btnRegistro.setGeometry((self.centralWidget().width() * (3 / 6)) + 10, 10, (self.centralWidget().width() * (1 / 6)) - 20, self.topMenuQw.height() - 20)
        self.btnIndice.setGeometry((self.centralWidget().width() * (4 / 6)) + 10, 10,(self.centralWidget().width() * (1 / 6)) - 20, self.topMenuQw.height() - 20)
        self.btnEstandarizacion.setGeometry((self.centralWidget().width() * (5 / 6)) + 10, 10,(self.centralWidget().width() * (1 / 6)) - 20, self.topMenuQw.height() - 20)

