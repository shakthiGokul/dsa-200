# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def findLoop(head):
#     slowNode , fastNode = head.next , head.next.next
#     while fastNode != slowNode:
#         slowNode = slowNode.next
#         fastNode = fastNode.next.next
#     fastNode = head
#     while fastNode != slowNode:
#         fastNode = fastNode.next
#         slowNode = slowNode.next
#     return slowNode    


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    currentNode = head
    prevNode = None
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode

def sortedSquaredArray(array):
    results = [0 for _ in array]
    leftBound = 0
    rightBound = len(array) - 1

    for idx in reversed(range(len(results))):
        if abs(array[leftBound]) <= abs(array[rightBound]):
            results[idx] = array[rightBound] * array[rightBound]
            rightBound -= 1
        else:
            results[idx] = array[leftBound] * array[leftBound]
            leftBound += 1
    return results