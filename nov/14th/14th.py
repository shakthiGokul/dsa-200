# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head ,node)    

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail , node)

    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
            
            

    def insertAfter(self, node, nodeToInsert):
        pass   

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                self.remove(currentNode)
            currentNode = currentNode.next    


    def remove(self, node):
        if node == self.head and self.head is not None:
            self.head = self.head.next
        elif node == self.tail and self.tail is not None:
            self.tail = self.tail.prev    
        self.removeNodeBindings(node)        

        
    def containsNodeWithValue(self, value):
        currentNode = self.head
        if currentNode is None:
            return
        while currentNode is not None and currentNode.value != value:
            currentNode = currentNode.next
        return currentNode is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev 
        # apply for head / tail nodes       
        node.next = None
        node.prev = None    
    
 