from LinkedList import *
class ArrayList():
    def __init__(self):
        self.lista = list()

    def print(self):
        print(self.lista)

    def get(self, index):
        return Node(self.lista[index - 1])

    def getData(self, index):
        return self.lista[index-1]

    def insertAtEnd(self, node):
        self.lista.append(node.data)

    def insertItemAtEnd(self, item):
        self.lista.append(item)

    def insertAtFront(self, node):
        self.lista.insert(0, node.data)

    def insertItemAtFront(self, item):
        self.lista.insert(0, item)

    def insertAtIndex(self, node, index):
        if (index > 0 and index <= self.size):
            self.lista.index(index-1,node.data)
        else:
            raise IndexError("Index out of bounds")

    def insertItemAtIndex(self, item, index):

        if (index > 0 and index <= (self.size + 1)):

            list.insert(index-1, item)
        else:
            print("index: " + str(index))
            print("self.size: " + str(self.size))
            raise IndexError("Index out of bounds")

    def deleteLast(self):
        self.lista.pop()

    def deleteFirst(self):
        self.lista.pop(0)


    def deleteAtIndex(self, index):
        self.lista.pop(index-1)


    def getSize(self):
        return len(self.lista)