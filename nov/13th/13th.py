# # # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def sumOfLinkedLists(linkedListOne, linkedListTwo):
# #     nodeOne = linkedListOne
# #     nodeTwo = linkedListTwo
# #     carry = 0
# #     node = LinkedList(-1)
# #     currentNode = node
# #     while nodeOne is not None or nodeTwo is not None or carry != 0:
# #         numberOne = nodeOne.value if nodeOne is not None else 0
# #         numberTwo = nodeTwo.value if nodeTwo is not None else 0
# #         currentSum = numberOne + numberTwo + carry
# #         currentDigit = currentSum % 10
# #         carry = currentSum // 10
# #         if currentNode:
# #             currentNode.next = LinkedList(currentDigit)
# #             currentNode = currentNode.next
# #         nodeOne = nodeOne.next if nodeOne is not None else None
# #         nodeTwo = nodeTwo.next if nodeTwo is not None else None
# #     return node.next

# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def mergingLinkedLists(linkedListOne, linkedListTwo):
# #     nodeOne = linkedListOne
# #     nodeTwo = linkedListTwo
# #     visitedNodes = set()
# #     while nodeOne is not None:
# #         visitedNodes.add(nodeOne)
# #         nodeOne = nodeOne.next
# #     while nodeTwo is not None:
# #         if nodeTwo in visitedNodes:
# #             return nodeTwo
# #         nodeTwo = nodeTwo.next    
# #     return None

# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     nodeOne = linkedListOne
#     nodeTwo = linkedListTwo
#     while nodeOne is not None or nodeTwo is not None:
#         if nodeOne == nodeTwo:
#             break
#         nodeOne = nodeOne.next if nodeOne is not None else linkedListTwo
#         nodeTwo = nodeTwo.next if nodeTwo is not None else linkedListOne
#     return nodeOne

def isPalindrome(string):
    leftBound , rightBound = 0 , len(string) - 1
    while leftBound <= rightBound:
        if string[leftBound] != string[rightBound]:
            return False
        leftBound += 1
        rightBound -= 1
    return True