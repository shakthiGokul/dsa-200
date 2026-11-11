# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def linkedListPalindrome(head):
#     slowNode = fastNode = head
#     while fastNode is not None and fastNode.next is not None:
#         slowNode = slowNode.next
#         fastNode = fastNode.next.next
#     nodeOne = reverseLinkedList(slowNode)
#     nodeTwo = head

#     while nodeOne is not None and nodeTwo is not None:
#         if nodeOne.value != nodeTwo.value:
#             return False
#         nodeOne = nodeOne.next
#         nodeTwo = nodeTwo.next  
#     return True

# def reverseLinkedList(head):
#     currentNode = head
#     prevNode = None
#     while currentNode is not None:
#         nextNode = currentNode.next
#         currentNode.next = prevNode
#         prevNode = currentNode
#         currentNode = nextNode
#     return prevNode

# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def zipLinkedList(linkedList):
#     fastNode = slowNode = linkedList
#     while fastNode is not None and fastNode.next is not None:
#         slowNode = slowNode.next
#         fastNode = fastNode.next.next
#     nodeTwo = reverseLinkedList(slowNode.next)
#     slowNode.next = None
#     nodeOne = linkedList

#     while nodeTwo is not None and nodeOne is not None:
#         tempOneNode = nodeOne.next
#         tempTwoNode = nodeTwo.next
#         nodeOne.next = nodeTwo
#         nodeTwo.next = tempOneNode
#         nodeOne = tempOneNode
#         nodeTwo = tempTwoNode  
#         if nodeTwo is not None:
#             nodeOne.next = nodeTwo
#         if nodeOne is not None:
#             nodeTwo.next = nodeOne    

#     return linkedList