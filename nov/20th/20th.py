# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    nodeTwo = LinkedList(-1)
    nodeOne = LinkedList(-1)
    currentNode = head
    currentNodeOne = nodeOne
    currentNodeTwo = nodeTwo
    while currentNode is not None and currentNode.next is not None:
        nextNode = currentNode.next
        currentNodeOne.next = currentNode
        currentNodeTwo.next = nextNode
        currentNodeOne = currentNodeOne.next
        currentNodeTwo = currentNodeTwo.next
        currentNode = nextNode.next
    currentNodeOne.next = currentNode
    currentNodeTwo.next = None
    currentNodeOne = nodeTwo.next
    currentNodeTwo = nodeOne.next
    node = LinkedList(-1)
    currentNode = node
    while currentNodeOne is not None and currentNodeTwo is not None:
        nextNodeOne = currentNodeOne.next
        nextNodeTwo = currentNodeTwo.next

        currentNode.next = currentNodeOne
        currentNodeOne.next = currentNodeTwo
        currentNode = currentNodeTwo

        currentNodeOne = nextNodeOne
        currentNodeTwo = nextNodeTwo
    currentNode.next = currentNodeOne if currentNodeOne is not None else currentNodeTwo
    
    return node.next