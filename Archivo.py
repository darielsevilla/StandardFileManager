import pickle
import traceback

from LinkedList import LinkedList, Node
from Campo import *
from pickle import *
from BinarySearchTree import *
from Registro import *
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
            self.btree2 = None
            self.btree3 = None
            self.metaSize = 0
            self.registerSize = 0

        def writeBTree(self):
            treePath = self.Path[:len(self.Path) - 3] + "dja"
            with open(treePath, 'wb') as file:
                pickle.dump(self.btree, file)
                pickle.dump(self.btree2, file)
                pickle.dump(self.btree3, file)

        def createBinarySearchTree(self):
            self.btree = BinarySearchTree(6)

            treePath = self.Path[:len(self.Path)-3] + "dja"
            with open(treePath, 'wb') as file:
                pickle.dump(self.btree, file)

        def loadBtree(self):
            isRead = False
            try:
                treePath = self.Path[:len(self.Path)-3] + "dja"

                with open(treePath, 'rb') as file:
                    self.btree = pickle.load(file)

                    self.btree2 = pickle.load(file)
                    self.btree3 = pickle.load(file)

                    return True
            except Exception as e:
                if self.btree != None:
                    return True
                return False
            
        def isRegisterWritten(self):
            return self.registerWritten

        def setRegisterWritten(self, boolean):
            self.registerWritten = boolean

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

            file = open(self.Path, 'r')
            try:
                metadata = file.readLine()

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
                
                #calculating size of register
                campos = self.Campos
                size = 0
                for i in range(self.Campos.getSize()):
                    size += self.Campos.get(i+1).getData().getFieldSize()
                self.registerSize = size+1


                #calculating size of offset
                self.metaSize = len(metadata)

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
                
            if(self.availist[0] == -1):
                stringav += "#####"
            else:
                pos = self.availist[0]
                stringav += str.rjust(str(pos),5,'#')

            isEmpty = str(int(self.registerWritten))


            with open(self.Path, 'r+') as file:
                file.seek(0)
                file.write(isEmpty)
                file.seek(2)
                file.write(regis)
                file.seek(0)
                file.seek(8)
                file.write(stringav)
                file.seek(0)
                currentLen = 14
                for i in range(self.Campos.getSize()):
                    currentLen += len(self.getCampo(i).getDataType()) + 1
                    currentLen += len(self.getCampo(i).getFieldName()) + 1
                    currentLen += len(str(self.getCampo(i).getFieldSize())) + 3

                    if self.getCampo(i).isSecondaryKey == True:
                        file.seek(currentLen)
                        file.write('1')
                    else:
                        currentLen += 1
                    currentLen += 1

            #updates numero de registros y primera posicion del availist

        def LoadFields(self):
            try:

                with open(self.Path, 'r') as file:
                    metadata = str(file.readline())
                self.charsMetadata = (len(metadata))
                tokens = metadata.split('|')
                self.registerWritten = bool(int(tokens[0]))

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

                    if (atts[4] == '0'):
                        field.isSecondaryKey = False
                    else:
                        field.isSecondaryKey = True
                    self.Campos.insertAtEnd(Node(field))

                if(tokens[2] == "#####"):
                    self.availist.append(-1)
                else:
                    first = tokens[2].replace("#","")
                    self.availist.append(int(first))

                 #calculating size of register
                campos = self.Campos
                size = 0
                for i in range(self.Campos.getSize()):
                    size += self.Campos.get(i+1).getData().getFieldSize()
                #self.registerSize = size+1
                self.registerSize = size

                #calculating size of offset
                self.metaSize = len(metadata)+1

                #self.guardarArchivo(metadata)
                #self.availist.append(int(-1))
                self.reloadAvailist()



            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e:
                return f"Error al cargar los campos del archivo: {str(e)}"

        def writeRegister(self, register):
            try:

                if(self.availist[0] == -1):

                    with open(self.Path, 'a') as file:
                        data = ""
                        for i in range(register.atributos.getSize()):
                            data += str(register.atributos.get(i+1).getData()).ljust(self.Campos.get(i+1).getData().getFieldSize())
                        #data +='\n'

                        key = register.getKey()
                        #if(isinstance(key,str)):
                        #    key = self.btree.stringToInt(key)
                        array = self.btree.insert(key, self.numeroDeRegistros)
                        if(array != False):

                            try:
                                self.btree.reorderTree(array[0], array[1])
                            except Exception as e:
                                traceback.print_exc()
                                sys.exit()
                            self.writeBTree()
                            file.write(data)
                            self.numeroDeRegistros += 1
                            self.registerWritten = True
                            self.updateMetaData()

                            return True
                        else:
                            return False
                else:
                    with open(self.Path, 'r+') as file:
                        rrn = self.availist[0]
                        offset = int(self.metaSize) + (int(self.registerSize) * int(rrn))

                        #writing data
                        file.seek(offset)

                        data = ""
                        for i in range(register.atributos.getSize()):
                            data += str(register.atributos.get(i+1).getData()).ljust(self.Campos.get(i+1).getData().getFieldSize())
                        #data+="\n"


                        key = register.getKey()
                        #if (isinstance(key, str)):
                        #    key = self.btree.stringToInt(key)
                        array = self.btree.insert(key, rrn)
                        if (array != False):

                            self.btree.reorderTree(array[0],array[1])
                            file.write(data)
                            self.availist.pop(0)

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
            

        def deleteRegister(self, key):
            rrn = self.btree.rrnSearch(key)


            if rrn == -1:
                return False
            with open(self.Path, 'r+') as file:
                offset = int(self.metaSize) + (int(self.registerSize) * int(rrn))

                file.seek(offset)
                self.availist.insert(0,rrn)
                #nextPos = "*"
                nextPos = str(self.availist[1])
                if nextPos == "-1":
                    nextPos = ""
                replacement = "|" +str(nextPos)

                for i in range(5-len(nextPos)):
                    replacement+="#"
                file.write(replacement)

                self.updateMetaData()


                try:
                    self.btree.deleteKey(key)
                    self.writeBTree()

                except Exception as e:
                    traceback.print_exc()

                return True #self.btree.deleteKey(key)

        def reloadAvailist(self):
            with open(self.Path, 'r') as file:

                rrn = self.availist[0]

                while rrn != -1:
                    file.seek(0)
                    file.seek(self.metaSize + (rrn*self.registerSize))
                    file.read(1)
                    strNextPos = file.read(5)
                    if strNextPos == "#####":
                        self.availist.append(-1)
                    else:
                        strNextPos = strNextPos.replace("#","")
                        self.availist.append(int(strNextPos))

                    rrn = self.availist[len(self.availist)-1]

        def loadRegistro(self, key, tipo):
            try:

                tree = None
                if tipo == self.btree.keyField:
                    tree = self.btree
                elif tipo == self.btree2.keyField:
                    tree = self.btree2
                elif tipo == self.btree3.keyField:
                    tree = self.btree3
                else:
                    return 2
                rrn = tree.rrnSearch(key)

                if rrn == -1:
                    return -1
                with open(self.Path, 'r') as file:
                    offset = int(self.metaSize) + (int(self.registerSize*rrn))

                    file.seek(0)
                    file.seek(offset)

                    registerStr = str(file.read(self.registerSize))
                    
                    if registerStr[0] == '|':
                        return 0
                    registro = Registro()
                    prevSize = 0
                    for x in range(self.Campos.getSize()):

                        type = self.getCampo(x).getDataType()

                        currentFieldSize = self.Campos.get(x+1).getData().getFieldSize()
                        currentField = registerStr[prevSize:+prevSize+currentFieldSize]

                        field = currentField.replace(' ','')

                        if type == "int":
                            field = int(field)
                        elif type == "float":
                            field = float(field)
                        else:
                            field = str(field)
                        registro.addAttribute(field)

                        if(self.getCampo(x).isKey()):
                            registro.setKey(field)
                        prevSize += currentFieldSize
                    return registro
            except Exception as e:
                traceback.print_exc()

        def modifyRegister(self, register):
            key = register.getKey()
            #if isinstance(key, str):
            #    key = self.btree.stringToInt(key)
            rrn = self.btree.rrnSearch(key)
            with open(self.Path, 'r+') as file:
                file.seek(self.metaSize + (self.registerSize*rrn))
                data = ""
                for i in range(register.atributos.getSize()):
                    data += str(register.atributos.get(i + 1).getData()).ljust(self.Campos.get(i + 1).getData().getFieldSize())
                file.write(data)
                return True
                # data +='\n'

        def fileDirectRead(self, rrn):
            try:
                if rrn == -1:
                    return -1
                with open(self.Path, 'r') as file:
                    offset = int(self.metaSize) + (int(self.registerSize * rrn))

                    file.seek(0)
                    file.seek(offset)

                    registerStr = str(file.read(self.registerSize))

                    if(registerStr[0] == '|'):
                        return -1
                    registro = Registro()
                    prevSize = 0
                    for x in range(self.Campos.getSize()):

                        type = self.getCampo(x).getDataType()

                        currentFieldSize = self.Campos.get(x + 1).getData().getFieldSize()
                        currentField = registerStr[prevSize:+prevSize + currentFieldSize]

                        field = currentField.replace(' ', '')

                        if type == "int":
                            field = int(field)
                        elif type == "float":
                            field = float(field)
                        else:
                            field = str(field)
                        registro.addAttribute(field)

                        if (self.getCampo(x).isKey()):
                            registro.setKey(field)
                        prevSize += currentFieldSize
                    return registro
            except Exception as e:
                traceback.print_exc()

        def indexSecondaryTree(self, node, btree, btree2, index):
            if node == None or node.keys.getSize() == 0:
                return -2
            for i in range(1, node.keys.getSize()+1):
                if node.sons.getSize() >= i:
                    btree2 = self.indexSecondaryTree(btree.nodes.getData(node.sons.getData(i)), btree,btree2,index)

                registro = self.loadRegistro(node.keys.getData(i), self.btree.keyField)

                key = registro.getAttribute(index).data
                if btree2 != -1:
                    if(btree2.rrnSearch(key) == -1):
                        array = btree2.insert(key, node.rrnList.getData(i))
                        btree2.reorderTree(array[0], array[1])
                    else:
                        return -1
                else:
                    return -1
            if node.sons.getSize() != 0:
                btree2 = self.indexSecondaryTree(btree.nodes.getData(node.sons.getData(node.sons.getSize())), btree, btree2, index)
            return btree2