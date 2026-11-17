# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    node = LinkedList(-1)
    nodeOne = headOne
    nodeTwo = headTwo
    currentNode = node
    while nodeOne is not None and nodeTwo is not None:
        valueOne = nodeOne.value
        valueTwo = nodeTwo.value
        if valueOne <= valueTwo:
            currentNode.next = nodeOne
            nodeOne = nodeOne.next
        else:
            currentNode.next = nodeTwo
            nodeTwo = nodeTwo.next
        currentNode = currentNode.next
    currentNode.next = nodeOne if nodeOne is not None else nodeTwo            
    return node.next
