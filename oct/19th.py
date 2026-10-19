# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(1) space 
def mergeLinkedLists(headOne, headTwo):
    node = LinkedList(-1)
    currentNode = node
    nodeOne = headOne
    nodeTwo = headTwo

    while nodeOne is not None and nodeTwo is not None:

        if nodeOne.value <= nodeTwo.value:
            currentNode.next = nodeOne
            nodeOne = nodeOne.next
        else:
            currentNode.next = nodeTwo
            currentNode.next = nodeTwo
            nodeTwo = nodeTwo.next
        currentNode = currentNode.next
    currentNode.next = nodeOne if nodeTwo is None else nodeTwo
    return node.next        