from Campo import *
class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None
    def __str__(self):
        return self.data
    def getData(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def print(self):
        currentNode = self.first

        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next

    def get(self, index):
        currentNode = self.first
        if (index > 0 and index <= self.size):
            for x in range(1, index):
                currentNode = currentNode.next
        else:
            return None
        return currentNode

    def insertAtEnd(self,node):
        currentNode = self.last
        if currentNode is None:
            self.last = node
            self.first = node
            self.size += 1
        else:
            node.previous = self.last
            self.last.next = node
            self.last = node
            self.size += 1
    
    def insertAtFront(self,node):
        currentNode = self.first
        if currentNode is None:
            self.last = node
            self.first = node
            self.size += 1
        else:
            node.next = currentNode
            self.first = node
            self.size += 1

    def insertAtIndex(self,node,index):
        if (index > 0 and index <= self.size):
            if(index == 1):
                self.insertAtFront(node)
            elif(index == self.size):
                self.insertAtEnd(node)
            else:
                currentNode = self.first
                for x in range(1,index):
                    currentNode = currentNode.next
                node.next = currentNode
                node.previous = currentNode.previous
                currentNode.previous.next = node
                currentNode.previous = node
            self.size += 1
        else:
            raise IndexError("Index out of bounds")
        
    def deleteLast(self):
        if self.last is None:
            return None
        else:
            currentNode = self.last
            self.last = currentNode.previous
            currentNode.previous.next = None
            currentNode = None
            self.size -= 1

    def deleteFirst(self):

        if self.first == None:
            return None
        else:
            currentNode = self.first

            if currentNode.next != None:

                self.first = currentNode.next
                self.first.previous = None
            else:
                self.first = None
                self.last = None

            currentNode = None
            self.size -= 1


    
    def deleteAtIndex(self,index):
        if(index > 0 and index <= self.size):
            if(index == 1):
                self.deleteFirst()
            elif(index == self.size):
                self.deleteLast()
            else:
                currentNode = self.first
                for x in range(1, index):
                    currentNode = currentNode.next
                currentNode.previous.next = currentNode.next
                currentNode.next.previous = currentNode.previous
                currentNode = None
                self.size -= 1

        else:
            raise IndexError("Index out of bounds")
    
    def updateNode(self,newData,index):
        currentNode = self.first
        if(index > 0 and index <= self.size):
            currentNode = self.first
            for x in range(1,index):
                currentNode = currentNode.next
            currentNode.data = newData
        else:
            raise IndexError("Index out of bounds")

    def getPrevious(self,node):
        return node.previous
    
    def getNext(self,node):
        return node.next

    def getSize(self):
        return self.size