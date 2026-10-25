class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.linkedList = DoublyLinkedList()
        self.currentSize = 0

    def insertKeyValuePair(self, key, value):
        newNode = DoublyLinkedListNode(key, value)
        if self.currentSize == self.maxSize:
            self.linkedList.removeNode()
            self.currentSize -= 1
        self.currentSize += 1        
        self.linkedList.setHead(newNode)
        self.cache[key] = newNode

    def getValueFromKey(self, key):
        if key in self.cache:
            return self.cache[key]

    def getMostRecentKey(self):
        head = self.linkedList.head
        return head
   


class DoublyLinkedList:
    def __init__(self):
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

    def removeNode(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(n) space
# def rearrangeLinkedList(head, k):
#     forwardNodes = []
#     backwardNodes = []
#     middleNodes = []
#     currentNode = head
#     while currentNode is not None:
#         if currentNode.value < k:
#             forwardNodes.append(currentNode)
#         elif currentNode.value > k:
#             backwardNodes.append(currentNode)
#         else:
#             middleNodes.append(currentNode)       
#         currentNode = currentNode.next
#     node = LinkedList(-1)
#     currentNode = node
#     for forwardNode in forwardNodes:
#         currentNode.next = forwardNode
#         currentNode = currentNode.next
#     for midNode in middleNodes:
#         currentNode.next = midNode
#         currentNode = currentNode.next
#     for backwardNode in backwardNodes:
#         currentNode.next = backwardNode
#         currentNode = currentNode.next
#     currentNode.next = None    
#     return node.next       
