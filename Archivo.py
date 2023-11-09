from LinkedList import LinkedList, Node
from Campo import *

class Archivo: 
        def __init__(self, nombre):
            self.Name = nombre
            self.Path = None
            self.Campos = LinkedList()
            self.registerEmpty = False
            self.availableSpaces = LinkedList()

        def isRegisterEmpty(self):
            return self.registerEmpty

        def setRegisterEmpty(self, boolean):
            self.registerEmpty = boolean
        def getName(self):
           return self.Name
        
        def getPath(self):
            return self.Path
        
        def getCampos(self):
            return self.Campos
            
        def setName(self, newName):
            self.Name = newName
        
        def setPath(self, newPath):
            self.Path = newPath
            
        def setCampos(self, newList):
            self.Campos = newList
            
        def abrirArchivo(self):
            try:
                with open(self.Path, 'r') as archivo:
                    contenido = archivo.read()
                return contenido
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e: 
                return f"Error al abrir el archivo: {str(e)}"
        
        def guardarArchivo(self, contenido = None):
            try:
                if(contenido == None):
                    file = open(self.Path, 'w')
                    file.close()
                with open(self.Path, 'a') as archivo:
                    if(contenido != None):
                        archivo.write(contenido)
                return "Archivo guardado exitosamente."
            except Exception as e: 
                return f"Error al guardar el archivo: {str(e)}"

        def insertCampo(self, campo):
            self.Campos.insertAtEnd(Node(campo))

        def getCampo(self, index):

            index = index+1
            node = self.Campos.get(index)

            if node != None:
                return node.data
            else:
                return None

        def deleteCampo(self, index):
            index = index + 1
            self.Campos.deleteAtIndex(index)

        def writeFields(self):
            print("insert code here")

