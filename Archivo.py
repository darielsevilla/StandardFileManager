import pickle
import traceback

from LinkedList import LinkedList, Node
from Campo import *
from pickle import *
from BinarySearchTree import *
import os
import sys

class Archivo: 
        def __init__(self, nombre):
            self.Name = nombre
            self.Path = None
            self.Campos = LinkedList()
            self.registerWritten = False
            self.availist = list()
            self.numeroDeRegistros = 0
            self.btree = None

        def writeBTree(self):
            treePath = self.Path[:len(self.Path) - 3] + "dja"
            with open(treePath, 'wb') as file:
                pickle.dump(self.btree, file)
        def createBinarySearchTree(self):
            self.btree = BinarySearchTree(4)

            treePath = self.Path[:len(self.Path)-3] + "dja"
            with open(treePath, 'wb') as file:
                pickle.dump(self.btree, file)

        def loadBtree(self):
            isRead = False
            try:

                treePath = self.Path[:len(self.Path)-3] + "dja"

                with open(treePath, 'rb') as file:
                    self.btree = pickle.load(file)


                    return True
            except Exception as e:
                return False
        def isRegisterWritten(self):
            return self.registerEmpty

        def setRegisterWritten(self, boolean):
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
        #registerEmpty|numeroDeRegistros|primerElementoArrayList|dataType$fieldName$fieldSize$isPKey$isSKey!dataType2$fieldName2$fieldSize2$isPKey$isSKey!|\n
            try:
                metadata = ""
                metadata += str(int(self.registerWritten)) + '|'
                #+str(self.numeroDeRegistros)+'|'
                if(self.numeroDeRegistros == 0):
                    metadata += "#####"
                else:
                    reg = str(self.numeroDeRegistros)
                    metadata += str.rjust(reg,5,'#')
                metadata += "|"
                metadata += "#####"
                metadata += "|"
                for x in range(self.Campos.getSize()):
                   currentNode = self.Campos.get(x+1)
                   if(x+1 == self.Campos.getSize()):
                       metadata += str(currentNode.getData().getDataType()) + '$' + str(currentNode.getData().getFieldName()) + '$' + str(currentNode.getData().getFieldSize()) + '$' + str(int(currentNode.getData().isKey())) + '$' + str(int(currentNode.getData().getSecondaryKey()))
                   else:
                       metadata += str(currentNode.getData().getDataType()) + '$' + str(currentNode.getData().getFieldName()) + '$' + str(currentNode.getData().getFieldSize()) + '$' + str(int(currentNode.getData().isKey())) + '$' + str(int(currentNode.getData().getSecondaryKey())) + '!'
                
                metadata += "|" + "\n"
                
                self.guardarArchivo(metadata)
                self.availist.append(int(-1))
                return "Información escrita en el archivo exitosamente."
            except Exception as e:

                return f"Error al escribir la información en el archivo: {str(e)}"

        def updateMetaData(self):
            regis = ""
            stringav = ""
            if(self.numeroDeRegistros == 0):
                regis += "#####"
            else:
                reg = str(self.numeroDeRegistros)
                regis += str.rjust(reg,5,'#')
                
            if(self.availist[-1] == -1):
                stringav += "#####"
            else:
                pos = self.availist[-1]
                stringav += str.rjust(str(pos),5,'#')

            isEmpty = str(int(self.registerWritten))

            with open(self.Path, 'r+') as file:
                file.seek(0)
                file.write(isEmpty)
                file.seek(2)
                file.write(regis)
                file.seek(8)
                file.write(stringav)
            #updates numero de registros y primera posicion del availist

        def LoadFields(self):
            try:

                with open(self.Path, 'r') as file:
                    metadata = str(file.readline())
                self.charsMetadata = (len(metadata))
                tokens = metadata.split('|')
                self.registerWritten = bool(tokens[0])

                if(tokens[1] == "#####"):
                    self.numeroDeRegistros = 0
                else:
                    regis = tokens[1].replace("#","")
                    self.numeroDeRegistros = int(regis)

                campos = tokens[3].split('!')
                for campo in campos:
                    atts = campo.split('$')
                    field = Campo(atts[0],atts[1],int(atts[2]))
                    if(atts[3] == '0'):
                        field.setKey(False)
                    else:
                        field.setKey(True)
                    self.Campos.insertAtEnd(Node(field))

                if(tokens[2] == "#####"):
                    self.availist.append(-1)
                else:
                    first = tokens[2].replace("#","")
                    self.availist.append(first)
                self.registerSize = 0
                for i in range(self.Campos.getSize()):
                    self.registerSize += self.Campos.get(i + 1).getData().getFieldSize()

                #hace falta implementar el llenado del arraylist
                self.reloadAvailist()
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e:
                return f"Error al cargar los campos del archivo: {str(e)}"

        def writeRegister(self, register):
            try:
                if(self.registerWritten == False):
                   self.availist.append(-1)

                if(self.availist[-1] == -1):

                    with open(self.Path, 'a') as file:
                        data = ""
                        for i in range(register.atributos.getSize()):
                            data += str(register.atributos.get(i+1).getData()).ljust(self.Campos.get(i+1).getData().getFieldSize())
                        data +='\n'

                        key = register.getKey()
                        if(isinstance(key,str)):
                            key = self.btree.stringToInt(key)

                        if(self.btree.insert(key, self.numeroDeRegistros) == True):
                            self.writeBTree()
                            file.write(data)
                            self.numeroDeRegistros += 1
                            self.registerWritten = True
                            self.updateMetaData()
                            self.btree.printBTree()
                            return True
                        else:
                            return False
                else:
                    with open(self.Path, 'r+') as file:
                        #calculating size of register
                        campos = self.Campos
                        size = 0
                        for i in range(self.Campos.getSize()):
                            size += self.Campos.get(i+1).getData().getFieldSize()
                        byteSize = size+1

                        rrn = self.availist[-1]

                        #calculating size of offset
                        metadata = str(file.readline())
                        metaSize = len(metadata)
                        offset = int(metaSize) + (int(byteSize) * int(rrn))

                        #writing data
                        file.seek(offset+1)
                        data = ""
                        for i in range(register.atributos.getSize()):
                            data += str(register.atributos.get(i+1).getData()).ljust(self.Campos.get(i+1).getData().getFieldSize())
                        data+="\n"


                        key = register.getKey()
                        if (isinstance(key, str)):
                            key = self.btree.stringToInt(key)
                        if (self.btree.insert(key, self.numeroDeRegistros) == True):
                            file.write(data)
                            self.availist.pop()
                            self.numeroDeRegistros += 1
                            self.registerWritten = True
                            self.writeBTree()
                            self.updateMetaData()
                            return True
                        else:
                            return False
            #still have to make availist
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e:
                traceback.print_exc()
                return f"Error al cargar los campos del archivo: {str(e)}"
            
            #self.btree.insert(register.getKey())
            #self.btree.printBTree()

        def deleteRegister(self, key):
            rrn = self.btree.rrnSearch(key)
            if rrn == -1:
                return False
            with open(self.Path, 'a') as file:
                #register size
                campos = self.Campos

                file.seek(self.charsMetadata+(self.registerSize*rrn))
                file.write("|")
                nextPos = str(self.availist[-1])
                if nextPos == "-1":
                    nextPos = ""
                for i in range(5-len(nextPos)):
                    nextPos += "#"
                file.write(nextPos)
                self.numeroDeRegistros -= 1
                self.availist.append(rrn)
                self.updateMetaData()

                #apartado de arbol
                return self.btree.deleteKey(key)

        def reloadAvailist(self):
            with open(self.Path, 'r') as file:
                while self.availist[-1] != -1:
                    file.seek(self.charsMetadata + (self.registerSize*self.availist[-1]))
                    file.read()
                    strNum = file.read(5)
                    strNum.replace("#", "")
                    if len(strNum) == 0:
                        self.availist.append(-1)
                    else:
                        self.availist.append(int(strNum))


