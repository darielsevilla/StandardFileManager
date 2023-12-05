import traceback
import numpy
from LinkedList import *
from ArrayList import ArrayList
class TreeNode():
    def __init__(self):
        self.keys = LinkedList()
        self.sons = LinkedList()
        self.rrnList = LinkedList()
        self.parent = None


class BinarySearchTree():
    def __init__(self, grado):
        self.keyField = None
        self.nodes = ArrayList()
        self.treeAvailist = LinkedList()
        self.rootPos = None
        self.root = None
        self.contador = 0
        self.grade = grado

    def insert(self, key, rrn, node=None, index=None):
        while(True):
            if(self.root != None and node == None):
                node = self.root
                index = self.rootPos
            if(self.nodes.getSize() == 0):
                #raiz no existe
                nodo = TreeNode()
                nodo.keys.insertItemAtEnd(key)
                nodo.rrnList.insertItemAtEnd(rrn)
                self.root = nodo
                self.rootPos = 1
                self.nodes.insertItemAtEnd(nodo)
                self.contador += 1
                array = [nodo, 1]
                return array
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
                    node.rrnList.insertItemAtIndex(rrn, position)
                    self.contador += 1
                    array = []
                    array.append(node)
                    array.append(index)
                    #self.reorderTree(node, index)
                    return array
                else:
                    return False

            else:
                #saca ultimo nodo de los hijos
                cont = node.sons.getData(node.sons.getSize())

                #recorre nodo buscando un valor mayor al de el, con un default del ultimo elemento
                for i in range(1, node.keys.getSize()+1):
                    if(node.keys.getData(i) > key):
                        cont = node.sons.getData(i)
                        break
                    if(node.keys.getData(i) == key):
                        return False
                restartNode = self.nodes.getData(cont)
                node = restartNode
                index = cont
                #return self.insert(key, rrn, restartNode, cont)

    def reorderTree(self, leafNode, cont):
        #print("cont" + str(cont))
        llaves = leafNode.keys
        nodePtrs = leafNode.sons
        rrns = leafNode.rrnList

        center = TreeNode()
        izquierda = TreeNode()
        derecha = TreeNode()

        indexLeft = 1
        indexRight = 1

        contadorNodes = 1
        contadorDerecha = 1

        while(llaves.getSize() > self.grade-1):
                #split del nodo
                particion = int(llaves.getSize()/2)
                if(llaves.getSize() % 2 != 0):
                    particion+=1
                for i in range(llaves.getSize()):
                    if(i+1 < particion):
                        izquierda.keys.insertItemAtIndex(llaves.getData(i+1),indexLeft)
                        izquierda.rrnList.insertItemAtIndex(rrns.getData(i+1), indexLeft)
                        indexLeft += 1

                        if(nodePtrs.getSize() != 0):
                            izquierda.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorNodes)

                            if(leafNode.parent == None):
                                #codigo medio medio
                                if(self.treeAvailist.getSize()>=1):
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.treeAvailist.getData(1)
                                else:
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 1
                            contadorNodes = contadorNodes + 1
                                #self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize()+1
                    elif (i+1 == particion):
                        center.keys.insertItemAtIndex(llaves.getData(i+1), 1)
                        center.rrnList.insertItemAtIndex(rrns.getData(i+1), 1)
                        if(nodePtrs.getSize() != 0):
                            izquierda.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorNodes)
                            if (leafNode.parent == None):
                                # codigo medio medio
                                if (self.treeAvailist.getSize() >= 1):
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.treeAvailist.getData(1)
                                else:
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 1
                            contadorNodes+=1
                    else:
                        derecha.keys.insertItemAtIndex(llaves.getData(i+1), indexRight)
                        derecha.rrnList.insertItemAtIndex(rrns.getData(i+1), indexRight)
                        indexRight+=1
                        if (nodePtrs.getSize() != 0):
                            derecha.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorDerecha)
                            if (leafNode.parent == None):
                                #codigo medio medio
                                if(self.treeAvailist.getSize()>=2):
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.treeAvailist.getData(2)
                                elif(self.treeAvailist.getSize() == 1):
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 1
                                else:
                                    self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 2
                                #self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 2
                            contadorNodes += 1
                            contadorDerecha += 1
                if(nodePtrs.getSize() != 0):
                    derecha.sons.insertItemAtIndex(nodePtrs.getData(contadorNodes), contadorDerecha)
                    if (leafNode.parent == None):
                        # codigo medio medio
                        if (self.treeAvailist.getSize() >= 2):
                            self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.treeAvailist.getData(2)
                        elif (self.treeAvailist.getSize() == 1):
                            self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 1
                        else:
                            self.nodes.getData(nodePtrs.getData(contadorNodes)).parent = self.nodes.getSize() + 2

                #ahora lo bonito

                #self.nodes.deleteAtIndex(cont)
                if(leafNode.parent == None):

                    izquierda.parent = cont
                    derecha.parent = cont
                    self.nodes.lista[cont-1] = center
                    #self.nodes.insertItemAtIndex(center, cont)
                    #codigo medio medio
                    if(self.treeAvailist.getSize() != 0):
                        #self.nodes.deleteAtIndex(self.treeAvailist.getData(1))
                        #self.nodes.insertItemAtIndex(izquierda, self.treeAvailist.getData(1))
                        self.nodes.lista[self.treeAvailist.getData(1)-1] = izquierda
                        center.sons.insertItemAtEnd(self.treeAvailist.getData(1))
                        self.treeAvailist.deleteAtIndex(1)
                    else:
                        self.nodes.insertItemAtEnd(izquierda)
                        center.sons.insertItemAtEnd(self.nodes.getSize())

                    if (self.treeAvailist.getSize() != 0):
                        #self.nodes.deleteAtIndex(self.treeAvailist.getData(1))
                        #self.nodes.insertItemAtIndex(derecha, self.treeAvailist.getData(1))
                        self.nodes.lista[self.treeAvailist.getData(1)-1] = derecha
                        center.sons.insertItemAtEnd(self.treeAvailist.getData(1))
                        self.treeAvailist.deleteAtIndex(1)
                    else:
                        self.nodes.insertItemAtEnd(derecha)
                        center.sons.insertItemAtEnd(self.nodes.getSize())

                    self.root = center
                    return True
                else:

                    self.nodes.lista[cont-1] = izquierda
                    for i in range(1,izquierda.sons.getSize()+1):
                        self.nodes.getData(izquierda.sons.getData(i)).parent = cont
                    #codigo medio medio
                    newPos = -1
                    if(self.treeAvailist.getSize() != 0):
                        newPos = self.treeAvailist.getData(1)
                        #self.nodes.deleteAtIndex(newPos)
                        #self.nodes.insertItemAtIndex(derecha,newPos)
                        self.nodes.lista[newPos-1] = derecha
                    else:
                        self.nodes.insertItemAtEnd(derecha)
                        newPos = self.nodes.getSize()
                    for i in range(1,derecha.sons.getSize()+1):
                        self.nodes.getData(derecha.sons.getData(i)).parent = newPos
                    #codigo funcional
                    #self.nodes.insertItemAtEnd(derecha)
                    parentTreeNode = self.nodes.getData(leafNode.parent)
                    posDePtr = -1
                    for i in range(1,parentTreeNode.sons.getSize()+1):
                        if(cont == parentTreeNode.sons.getData(i)):
                            posDePtr = i
                            break

                    #parentTreeNode.sons.deleteAtIndex(posDePtr)
                    parentTreeNode.keys.insertItemAtIndex(center.keys.getData(1), posDePtr)
                    parentTreeNode.rrnList.insertItemAtIndex(center.rrnList.getData(1), posDePtr)
                    #parentTreeNode.sons.insertItemAtIndex(cont, posDePtr)
                    # codigo medio medio
                    if (self.treeAvailist.getSize() != 0):

                        parentTreeNode.sons.insertItemAtIndex(self.treeAvailist.getData(1), posDePtr + 1)
                        self.treeAvailist.deleteAtIndex(1)
                    else:
                        parentTreeNode.sons.insertItemAtIndex(self.nodes.getSize(), posDePtr+1)

                    izquierda.parent = leafNode.parent
                    derecha.parent = leafNode.parent
                    cont = leafNode.parent
                    leafNode = parentTreeNode

                    llaves = leafNode.keys
                    nodePtrs = leafNode.sons
                    rrns = leafNode.rrnList

                    center = TreeNode()
                    izquierda = TreeNode()
                    derecha = TreeNode()

                    indexLeft = 1
                    indexRight = 1

                    contadorNodes = 1
                    contadorDerecha = 1
                    #return self.reorderTree(parentTreeNode, leafNode.parent)

    def rrnSearch(self, key, node = None):
        if (self.root != None and node == None):
            node = self.root
        if (self.nodes.getSize() == 0):
            # raiz no existe
            return -1
        elif (node.sons.getSize() == 0):
            # entra si el nodo actual no tiene hijos, saca ultima posicion
            position = node.keys.getSize() + 1
            for i in range(1, node.keys.getSize() + 1):
                if(node.keys.getData(i) == key):
                    return node.rrnList.getData(i)
            return -1
        else:
            # saca ultimo nodo de los hijos
            cont = node.sons.getData(node.sons.getSize())

            # recorre nodo buscando un valor mayor al de el, con un default del ultimo elemento
            for i in range(1, node.keys.getSize() + 1):

                if (node.keys.getData(i) > key):
                    cont = node.sons.getData(i)
                    break
                elif(node.keys.getData(i) == key):
                    return node.rrnList.getData(i)
            restartNode = self.nodes.getData(cont)

            return self.rrnSearch(key, restartNode)

    def nodePosSearch(self, key, node = None, pos = None):
        try:
            if (self.root != None and node == None):
                node = self.root
                pos = 1
            if (self.nodes.getSize() == 0):
                # raiz no existe
                return -1
            elif (node.sons.getSize() == 0):
                # entra si el nodo actual no tiene hijos, saca ultima posicion
                position = node.keys.getSize() + 1
                for i in range(1, node.keys.getSize() + 1):
                    if (node.keys.getData(i) == key):
                        return pos
                return -1
            else:
                # saca ultimo nodo de los hijos
                pos2 = node.sons.getData(node.sons.getSize())

                # recorre nodo buscando un valor mayor al de el, con un default del ultimo elemento
                for i in range(1, node.keys.getSize() + 1):
                    if (node.keys.getData(i) > key):
                        pos2 = node.sons.getData(i)
                        break
                    elif(node.keys.getData(i) == key):
                        return pos
                restartNode = self.nodes.getData(pos2)

                return self.nodePosSearch(key, restartNode, pos2)
        except Exception as e:
            traceback.print_exc()

    def deleteKey(self, key, node = None, nodePos = None):
        try:
            copyNode = node
            copyPos = nodePos
            minimum = int((self.grade-1)/2)
            if(nodePos == None):
                nodePos = self.nodePosSearch(key)
            if(nodePos == -1):
                return False

            if(node == None):
                node = self.nodes.getData(nodePos)
            if(copyPos == None and copyNode == None):
                self.contador -= 1
            #listas redeclaradas para acortar sintaxis
            keys = node.keys
            sons = node.sons
            rrns = node.rrnList

            #si nodo no tiene hijos
            if(node.sons.getSize() == 0):
                #deletion
                for i in range(1, keys.getSize()+1):
                    if keys.getData(i) == key:
                        keys.deleteAtIndex(i)
                        rrns.deleteAtIndex(i)
                        break
                try:
                    self.reorderPostDeletion(node, nodePos)
                except Exception as e:
                    traceback.print_exc()
            else:

                posDeKey = -1

                for i in range(1, keys.getSize() + 1):
                    if keys.getData(i) == key:
                        posDeKey = i
                        break
                posicion = sons.getData(posDeKey)
                data = self.getGreatestNode(self.nodes.getData(posicion), posicion)
                sonNode = data[0]
                posicion = data[1]
                keysDeHijo = sonNode.keys


                currentRRN = rrns.getData(posDeKey)

                node.keys.get(posDeKey).data = sonNode.keys.getData(sonNode.keys.getSize())
                node.rrnList.get(posDeKey).data = sonNode.rrnList.getData(sonNode.rrnList.getSize())
                sonNode.keys.get(sonNode.keys.getSize()).data = key
                sonNode.rrnList.get(sonNode.keys.getSize()).data = currentRRN
                return self.deleteKey(key, sonNode, posicion)


            return True
        except Exception as e:
            traceback.print_exc()
    def reorderPostDeletion(self, node, nodePos):
        try:
            keys = node.keys
            sons = node.sons
            rrns = node.rrnList
            #print("APENAS BORRADO:")
            #self.printBTree()

            minimum = int((self.grade -1) / 2)
            if node != self.root and node.keys.getSize() < minimum:
                # saca el padre
                parentNode = self.nodes.getData(node.parent)
                posDeHijo = -1
                keyToMoveIndex = -1
                for i in range(1, parentNode.sons.getSize() + 1):
                    if parentNode.sons.getData(i) == nodePos:
                        posDeHijo = i
                        break
                # compara los hijos
                # consigue posicion de hijo en la lista de hijos, no en la lista de nodo
                # seleccion de pos de nuevo nodo
                if posDeHijo - 1 > 0 and posDeHijo + 1 <= parentNode.sons.getSize():
                    behind = False
                    # cantidad de keys de los nodos a la izquierda y derecha
                    keysLeft = self.nodes.getData(parentNode.sons.getData(posDeHijo - 1)).keys.getSize()
                    keysRight = self.nodes.getData(parentNode.sons.getData(posDeHijo + 1)).keys.getSize()
                    if (keysRight > keysLeft):
                        # saca el padre de la derecha, y lo mueve al vecino derecho
                        keyToMoveIndex = parentNode.sons.getData(posDeHijo + 1)
                        node.keys.insertItemAtEnd(parentNode.keys.getData(posDeHijo))
                        rrns.insertItemAtEnd(parentNode.rrnList.getData(posDeHijo))
                        parentNode.keys.deleteAtIndex(posDeHijo)
                        parentNode.rrnList.deleteAtIndex(posDeHijo)
                        parentNode.sons.deleteAtIndex(posDeHijo)

                        behind = False
                    else:
                        # saca el padre de la izquierda y lo mueve al vecino izquierdo
                        keyToMoveIndex = parentNode.sons.getData(posDeHijo - 1)
                        node.keys.insertItemAtFront(parentNode.keys.getData(posDeHijo - 1))
                        rrns.insertItemAtFront(parentNode.rrnList.getData(posDeHijo - 1))
                        parentNode.keys.deleteAtIndex(posDeHijo - 1)
                        parentNode.rrnList.deleteAtIndex(posDeHijo - 1)
                        parentNode.sons.deleteAtIndex(posDeHijo)
                        behind = True
                elif posDeHijo - 1 > 0:
                    keyToMoveIndex = parentNode.sons.getData(posDeHijo - 1)
                    node.keys.insertItemAtFront(parentNode.keys.getData(posDeHijo - 1))
                    rrns.insertItemAtFront(parentNode.rrnList.getData(posDeHijo - 1))
                    parentNode.keys.deleteAtIndex(posDeHijo - 1)
                    parentNode.rrnList.deleteAtIndex(posDeHijo - 1)
                    parentNode.sons.deleteAtIndex(posDeHijo)
                    behind = True
                elif posDeHijo + 1 <= parentNode.sons.getSize():
                    keyToMoveIndex = parentNode.sons.getData(posDeHijo + 1)
                    node.keys.insertItemAtEnd(parentNode.keys.getData(posDeHijo))
                    rrns.insertItemAtEnd(parentNode.rrnList.getData(posDeHijo))
                    parentNode.keys.deleteAtIndex(posDeHijo)
                    parentNode.rrnList.deleteAtIndex(posDeHijo)
                    parentNode.sons.deleteAtIndex(posDeHijo)
                    behind = False
                nuevoNodo = self.nodes.getData(keyToMoveIndex)
                for i in range(1, node.sons.getSize() + 1):
                    self.nodes.getData(node.sons.getData(i)).parent = keyToMoveIndex


                # merge nodes to the most populated cousin
                for i in range(node.keys.getSize()):
                    if behind == True:
                        nuevoNodo.keys.insertItemAtEnd(node.keys.getData(i+1))
                        nuevoNodo.rrnList.insertItemAtEnd(node.rrnList.getData(i+1))
                        if node.sons.getSize() != 0:
                            nuevoNodo.sons.insertItemAtEnd(node.sons.getData(i+1))
                    else:
                        nuevoNodo.keys.insertItemAtFront(node.keys.getData(node.keys.getSize() - i))
                        nuevoNodo.rrnList.insertItemAtFront(node.rrnList.getData(node.rrnList.getSize() - i))
                        if node.sons.getSize() != 0:
                            nuevoNodo.sons.insertItemAtFront(node.sons.getData(node.rrnList.getSize() - i))

                self.treeAvailist.insertItemAtEnd(nodePos)
                # en teoria, hasta aqui esta bien ^^

                if nuevoNodo.keys.getSize() > self.grade - 1:
                    self.reorderTree(nuevoNodo, keyToMoveIndex)
                elif parentNode.keys.getSize() == 0 and parentNode == self.root:
                    self.root = nuevoNodo
                    self.nodes.lista[0] = nuevoNodo
                    for i in range(1,1+nuevoNodo.sons.getSize()):
                        self.nodes.getData(nuevoNodo.sons.getData(i)).parent = 1
                    self.reorderTree(nuevoNodo, 1)
                elif parentNode.keys.getSize() < minimum:
                    self.reorderPostDeletion(parentNode, node.parent)
        except Exception as e:
            traceback.print_exc()
    def listRRN(self, node = None, list = None, count = 0):
        if self.nodes.getSize() == 0:
            return -1
        if list == None and node == None:
            list = []
            node = self.root


        for i in range(1,node.keys.getSize()+1):

            if(node.sons.getSize() >= i):
                list = self.listRRN(self.nodes.getData(node.sons.getData(i)), list, count)
                count = len(list)
            if count >= 10:
                return list

            list.append(node.rrnList.getData(i))
            count += 1
            if count >= 10:
                return list
        if node.sons.getSize() != 0:
            list = self.listRRN(self.nodes.getData(node.sons.getData(node.sons.getSize())),list, count)
        return list

    def getGreatestNode(self, node, pos):
        if node.sons.getSize() != 0:
            data = node.sons.getData(node.sons.getSize())
            return self.getGreatestNode(self.nodes.getData(data), data)
        return [node, pos]
    def printBTree(self):
        print("\n\n\n\n\n")
        print("INICIO")
        for i in range(self.nodes.getSize()):
            isDeleted = False
            print(i+1)
            for j in range(self.treeAvailist.getSize()):
                if i+1 == self.treeAvailist.getData(j):
                    isDeleted = True
            if isDeleted == False:
                if(self.nodes.getData(i+1).parent != None):
                    print("parent: " + str(self.nodes.getData(i+1).parent))
                else:
                    print("root")
                print("keys----------------------------------------------")
                treeNode = self.nodes.getData(i+1)
                for j in range(treeNode.keys.getSize()):
                    print(str(treeNode.keys.getData(j+1)),end=" ")
                print("\nsons----------------------------------------------")
                for k in range(treeNode.sons.getSize()):
                    print(str(self.nodes.getData(i + 1).sons.getData(k + 1)),end=" ")
                print("\nrrns----------------------------------------------")
                for k in range(treeNode.rrnList.getSize()):
                    print(self.nodes.getData(i + 1).rrnList.getData(k + 1),end=" ")
                print(" ")
            else:
                print("*casilla borrada*")
        print("FIN")
