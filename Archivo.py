from LinkedList import LinkedList, Node
from Campo import *
import os

class Archivo: 
        def __init__(self, nombre):
            self.Name = nombre
            self.Path = None
            self.Campos = LinkedList()
            self.registerEmpty = False
            self.availableSpaces = LinkedList()
            self.numeroDeRegistros = 0
            self.charsMetadata = 0

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

        def abrirArchivo2(self):
            print(self.Path)
            file = open(self.Path, 'r')
            try:
                metadata = file.readLine()
                print(metadata)
            except Exception as e:
                return f"Error al abrir el archivo: {str(e)}"
            finally:
                file.close() 
                
            
        def abrirArchivo(self):
            try:
                self.LoadFields()
                with open(self.Path, 'r') as file:
                        contenido = file.read()
                return contenido
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e: 
                return f"Error al abrir el archivo: {str(e)}"
        
        def guardarArchivo(self, contenido = None):
            try:
                file = open(self.Path, 'w')
                if(contenido is not None):
                    file.write(contenido)
                return "Archivo guardado exitosamente."
                file.close()
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
        #registerEmpty|numeroDeRegistros|dataType$fieldName$fieldSize$isPKey$isSKey!dataType2$fieldName2$fieldSize2$isPKey$isSKey!|primerElementoArrayList|\n
            try:
                metadata = ""
                metadata += str(int(self.registerEmpty)) + '|'
                #+str(self.numeroDeRegistros)+'|'
                if(self.numeroDeRegistros == 0):
                    metadata += "#####"
                else:
                    reg = str(self.numeroDeRegistros)
                    metadata += str.rjust(reg,5,'#')
                metadata += "|"

                for x in range(self.Campos.getSize()):
                   currentNode = self.Campos.get(x+1)
                   if(x+1 == self.Campos.getSize()):
                       metadata += str(currentNode.getData().getDataType()) + '$' + str(currentNode.getData().getFieldName()) + '$' + str(currentNode.getData().getFieldSize()) + '$' + str(int(currentNode.getData().isKey())) + '$' + str(int(currentNode.getData().getSecondaryKey()))
                   else:
                       metadata += str(currentNode.getData().getDataType()) + '$' + str(currentNode.getData().getFieldName()) + '$' + str(currentNode.getData().getFieldSize()) + '$' + str(int(currentNode.getData().isKey())) + '$' + str(int(currentNode.getData().getSecondaryKey())) + '!'
                metadata += '|'
                if(self.availableSpaces.getSize() == 0):
                    metadata += "#####"
                else:
                    pos = str(self.availableSpaces.get(1))
                    metadata += str.rjust(pos,5,'#')
                metadata += "|" + "\n"
                
                self.guardarArchivo(metadata)
                
                self.charsMetadata = (len(metadata))
                return "Información escrita en el archivo exitosamente."
            except Exception as e:
                return f"Error al escribir la información en el archivo: {str(e)}"
            
        def LoadFields(self):
            try:
                with open(self.Path, 'r') as file:
                    metadata = str(file.readline())
                self.charsMetadata = (len(metadata))
                tokens = metadata.split('|')
                self.isRegisterEmpty = tokens[0]

                if(tokens[1] == "#####"):
                    self.numeroDeRegistros = 0
                else:
                    regis = tokens[1].replace("#","")
                    self.numeroDeRegistros = int(tokens[1])

                campos = tokens[2].split('!')
                for campo in campos:
                    atts = campo.split('$')
                    field = Campo(atts[0],atts[1],int(atts[2]))
                    field.setKey(atts[3])
                    self.Campos.insertAtEnd(Node(field))

                if(tokens[3] == "#####"):
                    self.availableSpaces.insertAtEnd(Node(-1))
                else:
                    spaces = tokens[3].replace("#","")
                    self.availableSpaces.insertAtFront(Node(int(spaces)))
                print(self.availableSpaces.get(1))
                #hace falta implementar el llenado del arraylist
                
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e:
                return f"Error al cargar los campos del archivo: {str(e)}"  
                    