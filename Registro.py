from LinkedList import *
class Registro():
    def __init__(self):
        self.atributos = LinkedList()
        self.primaryKey = None

    def addAttribute(self, attribute):
        self.atributos.insertAtEnd(Node(attribute))

    def getAttribute(self, index):
        return self.atributos.get(index+1)

    def setKey(self, key):
        self.primaryKey = key

    def getKey(self):
        return self.primaryKey