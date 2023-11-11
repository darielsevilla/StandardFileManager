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
                        file.close()
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

        def writeFields(self,campo):
            try:
                nuevoContenido = []
                nuevoContenido.append(f"Registro Vacío: {str(self.registerEmpty)}")
                nuevoContenido.append(f"Contador de Registros: {str(len(self.Campos))}")

                camposEncabezado = "|".join(campo.getFieldName() for campo in self.Campos)
                nuevoContenido.append(f"Campos: {camposEncabezado}")

                for registro in self.Registros:
                    dato = registro.getDataForCampo(campo)   
                    nuevoContenido.append(str(dato))

                primerEspacio = self.availableSpaces.get(1)
                nuevoContenido.append(f"Primer Espacio Disponible: {str(primerEspacio)}")

                self.guardarArchivo('\n'.join(nuevoContenido))
                
                return "Información escrita en el archivo exitosamente."
            except Exception as e:
                return f"Error al escribir la información en el archivo: {str(e)}"
            
            def LoadFields(self):
                print("F")
                    