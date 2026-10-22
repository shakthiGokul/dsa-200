class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        pass

    def getValueFromKey(self, key):
        # Write your code here.
        pass

    def getMostRecentKey(self):
        # Write your code here.
        pass

class Node:
    def __int__(self):
        self.prev = None
        self.next = None
        self.value = None

class DoublyLinkedList:
    def __int__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node 
            return 
       
        if self.head == self.tail:
            node.next = self.tail
            self.head.prev = node
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
