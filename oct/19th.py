# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# # O(n + m) time | O(1) space 
# def mergeLinkedLists(headOne, headTwo):
#     node = LinkedList(-1)
#     currentNode = node
#     nodeOne = headOne
#     nodeTwo = headTwo

#     while nodeOne is not None and nodeTwo is not None:

#         if nodeOne.value <= nodeTwo.value:
#             currentNode.next = nodeOne
#             nodeOne = nodeOne.next
#         else:
#             currentNode.next = nodeTwo
#             currentNode.next = nodeTwo
#             nodeTwo = nodeTwo.next
#         currentNode = currentNode.next
#     currentNode.next = nodeOne if nodeTwo is None else nodeTwo
#     return node.next

# # This is the class of the input linked list.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def shiftLinkedList(head, k):
#     listTail = head
#     totalLength = 1

#     while listTail is not None and listTail.next is not None:
#         listTail = listTail.next
#         totalLength += 1
#     offset = abs(k) % totalLength
#     if offset == 0:
#         return head
#     newTailPoint = totalLength - offset if k > 0 else offset
#     newTail = head

#     for _ in range(1 , newTailPoint):
#         newTail = newTail.next
#     newHead = newTail.next
#     newTail.next = None
#     if listTail is not None:
#         listTail.next = head
#     return newHead 