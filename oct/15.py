# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def sumOfLinkedLists(linkedListOne, linkedListTwo):
#     node = LinkedList(-1)
#     currentNode = node
#     nodeOne = linkedListOne
#     nodeTwo = linkedListTwo
#     carry = 0 
#     while nodeOne is not None or nodeTwo is not None or carry !=0:
#         valueOne = nodeOne.value if nodeOne is not None else 0
#         valueTwo = nodeTwo.value if nodeTwo is not None else 0
#         sumOfValue = valueOne + valueTwo + carry
#         carry = sumOfValue // 10
#         digit = sumOfValue % 10
#         if currentNode:
#             currentNode.next = LinkedList(digit)
#             currentNode = currentNode.next
#         nodeOne = nodeOne.next if nodeOne is not None else None
#         nodeTwo = nodeTwo.next if nodeTwo is not None else None
#     return node.next

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(n) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    nodeOne = linkedListOne
    nodes = set()
    while nodeOne is not None:
        nodes.add(nodeOne)
        nodeOne = nodeOne.next
    nodeTwo = linkedListTwo
    while nodeTwo is not None:
        if nodeTwo in nodes:
            break
        nodeTwo = nodeTwo.next    
    return nodeTwo