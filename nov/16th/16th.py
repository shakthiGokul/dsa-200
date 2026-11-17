# # # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def mergeLinkedLists(headOne, headTwo):
# #     node = LinkedList(-1)
# #     nodeOne = headOne
# #     nodeTwo = headTwo
# #     currentNode = node
# #     while nodeOne is not None and nodeTwo is not None:
# #         valueOne = nodeOne.value
# #         valueTwo = nodeTwo.value
# #         if valueOne <= valueTwo:
# #             currentNode.next = nodeOne
# #             nodeOne = nodeOne.next
# #         else:
# #             currentNode.next = nodeTwo
# #             nodeTwo = nodeTwo.next
# #         currentNode = currentNode.next
# #     currentNode.next = nodeOne if nodeOne is not None else nodeTwo            
# #     return node.next


# # This is the class of the input linked list.
# # This is the class of the input linked list.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def shiftLinkedList(head, k):
#     totalLength = 1
#     currentNode = head
#     while currentNode is not None and currentNode.next is not None:
#         totalLength += 1
#         currentNode = currentNode.next
#     offset = abs(k) % totalLength
#     if offset == 0:
#         return head
#     newTailPosition = totalLength - offset if k > 0 else offset
#     nodeOne = head
#     for _ in range(1,newTailPosition):
#         nodeOne = nodeOne.next 
#     node = nodeOne.next
#     nodeOne.next = None
#     currentNode.next = head
#     return node    
   
