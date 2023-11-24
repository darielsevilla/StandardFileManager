from LinkedList import *

class TreeNode():
    def __init__(self):
        self.keys = LinkedList()
        self.sons = LinkedList()
        self.parent = None
        self.rrn = None

class BinarySearchTree():
    def __init__(self, grado):
        self.nodes = LinkedList()
        self.rootPos = None
        self.root = None
        self.grade = grado

    def insert(self, key, node=None, index=None):

        if(self.root != None and node == None):
            node = self.root
            index = self.rootPos
        if(self.nodes.getSize() == 0):
            #raiz no existe
            nodo = TreeNode()
            nodo.keys.insertItemAtEnd(key)
            self.root = nodo
            self.rootPos = 1
            self.nodes.insertItemAtEnd(nodo)
        elif(node.sons.getSize() == 0):
            #entra si el nodo actual no tiene hijos, saca ultima posicion
            position = node.keys.getSize()+1
            iguales = False
            updated = False
            for i in range(1, node.keys.getSize()+1):
                iguales = False

                #si encuentra una llave mayor, se inserta en su lugar y corre
                if(node.keys.getData(i) > key and updated == False):
                    position = i
                    break
                elif(node.keys.getData(i) == key):
                    iguales = True
                if(updated == True or iguales == True):
                    break
            if(iguales != True):
                node.keys.insertItemAtIndex(key, position)



        else:
            #saca ultimo nodo de los hijos
            cont = node.sons.getData(node.sons.getSize())

            #recorre nodo buscando un valor mayor al de el, con un default del ultimo elemento
            for i in range(1, node.keys.getSize()+1):
                if(node.keys.getData(i) > key):
                    cont = node.sons.getData(i)
                    break
            restartNode = self.nodes.getData(cont)

            self.insert(key, restartNode, cont)
        if(node != None):
            self.reorderTree(node, index)

    def reorderTree(self, leafNode, cont):
        llaves = leafNode.keys
        nodePtrs = leafNode.sons

        center = TreeNode()
        izquierda = TreeNode()
        derecha = TreeNode()

        indexLeft = 1
        indexRight = 1

        contadorNodes = 1
        contadorDerecha = 1

        if(llaves.getSize() > self.grade-1):
                #split del nodo
                particion = int(llaves.getSize()/2)
                if(llaves.getSize() % 2 != 0):
                    particion+=1
                for i in range(llaves.getSize()):
                    if(i+1 < particion):
                        izquierda.keys.insertItemAtIndex(llaves.getData(i+1),indexLeft)
                        indexLeft += 1

                        if(nodePtrs.getSize() != 0):
                            izquierda.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorNodes)
                            contadorNodes = contadorNodes + 1
                            if(leafNode.parent == None):
                                self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize()+1
                    elif (i+1 == particion):
                        center.keys.insertItemAtIndex(llaves.getData(i+1), 1)
                        if(nodePtrs.getSize() != 0):
                            izquierda.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorNodes)
                            contadorNodes+=1
                    else:
                        derecha.keys.insertItemAtIndex(llaves.getData(i+1), indexRight)
                        indexRight+=1
                        if (nodePtrs.getSize() != 0):
                            derecha.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorDerecha)
                            contadorNodes += 1
                            contadorDerecha+=1
                            if (leafNode.parent == None):
                                self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 2

                if(nodePtrs.getSize() != 0):
                    derecha.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorDerecha)

                #ahora lo bonito

                self.nodes.deleteAtIndex(cont)
                #self.nodes.insertItemAtIndex(izquierda,cont)
                #self.nodes.insertItemAtEnd(izquierda)
                #self.nodes.insertItemAtEnd(derecha)

                if(leafNode.parent == None):

                    izquierda.parent = cont
                    derecha.parent = cont
                    self.nodes.insertItemAtIndex(center, cont)
                    self.nodes.insertItemAtEnd(izquierda)
                    self.nodes.insertItemAtEnd(derecha)
                    center.sons.insertItemAtEnd(self.nodes.getSize()-1)
                    center.sons.insertItemAtEnd(self.nodes.getSize())
                    self.root = center
                else:

                    self.nodes.insertItemAtIndex(izquierda, cont)
                    # self.nodes.insertItemAtEnd(izquierda)
                    self.nodes.insertItemAtEnd(derecha)
                    parentTreeNode = self.nodes.getData(leafNode.parent)
                    posDePtr = -1
                    for i in range(1,parentTreeNode.sons.getSize()+1):
                        if(cont == parentTreeNode.sons.getData(i)):
                            posDePtr = i
                            break
                    parentTreeNode.sons.deleteAtIndex(posDePtr)
                    parentTreeNode.keys.insertItemAtIndex(center.keys.getData(1), posDePtr)
                    parentTreeNode.sons.insertItemAtIndex(cont, posDePtr)
                    parentTreeNode.sons.insertItemAtIndex(self.nodes.getSize(), posDePtr+1)
                    izquierda.parent = leafNode.parent
                    derecha.parent = leafNode.parent
                    self.reorderTree(parentTreeNode, leafNode.parent)

    def stringToInt(self, string):
        uniqueKey = 0
        factor = 1
        for i in string:
            uniqueKey += factor*ord(i)
            factor += 1


    def printBTree(self):
        print("INICIO")
        for i in range(self.nodes.getSize()):


            print("keys----------------------------------------------")
            treeNode = self.nodes.getData(i+1)
            for j in range(treeNode.keys.getSize()):
                print(treeNode.keys.getData(j+1))
            print("sons----------------------------------------------")
            for k in range(treeNode.sons.getSize()):
                print(self.nodes.getData(i + 1).sons.getData(k + 1))
        print("FIN")