# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(n) time | O(1) space
# # def removeDuplicatesFromLinkedList(linkedList):
# #     nodeOne = nodeTwo = linkedList
# #     while nodeTwo is not None:
# #         if nodeOne.value != nodeTwo.value:
# #             nodeOne.next = nodeTwo
# #             nodeOne = nodeTwo
# #         nodeTwo = nodeTwo.next
# #     nodeOne.next = None        
# #     return linkedList        

# def removeDuplicatesFromLinkedList(linkedList):
#     currentNode = linkedList

#     while currentNode is not None:
#         nextDistinctNode = currentNode.next

#         while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
#             nextDistinctNode = nextDistinctNode.next
#         currentNode.next = nextDistinctNode
#         currentNode = nextDistinctNode
#     return linkedList

# # This is an input class. Do not edit.

# # O(n) time | O(1) space
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def middleNode(linkedList):
#     slow = fast = linkedList

#     while fast is not None and fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next
#     return slow    