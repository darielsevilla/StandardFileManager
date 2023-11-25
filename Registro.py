from LinkedList import *
from Archivo import Archivo
import os

class Registro():
    def __init__(self):
        self.atributos = LinkedList()
        self.primaryKey = None
        self.maxlengths = []

    def addAttribute(self, attribute):
        self.atributos.insertAtEnd(Node(attribute))

    def getAttribute(self, index):
        return self.atributos.get(index+1)

    def setKey(self, key):
        self.primaryKey = key

    def getKey(self):
        return self.primaryKey
    
    #5684
    def insertRegistro(self, file):
        try:
            data = ""
            for i in range(self.atributos.getSize()):
                cont = str(self.atributos(i+1))
                data += cont.ljust(self.maxlengths(1))
            data +='\n'
            file.appendInfo(data)
            return "Información escrita en el archivo exitosamente."
        except Exception as e:
            return f"Error al escribir la información en el archivo: {str(e)}"