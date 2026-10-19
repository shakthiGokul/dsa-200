# # # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def findLoop(head):
# #     slowNode = head.next
# #     fastNode = head.next.next

# #     while fastNode is not None and fastNode.next is not None and slowNode != fastNode:
# #         slowNode = slowNode.next
# #         fastNode = fastNode.next.next

# #     fastNode = head

# #     while fastNode is not None and slowNode is not None and slowNode != fastNode:
# #         slowNode = slowNode.next
# #         fastNode = fastNode.next
# #     return slowNode        


# # # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def reverseLinkedList(head):
# #     prevNode = None
# #     currentNode = head

# #     while currentNode is not None:
# #         nextNode = currentNode.next
# #         currentNode.next = prevNode
# #         prevNode = currentNode
# #         currentNode = nextNode
# #     return prevNode

# def nonConstructibleChange(coins):
#     coins.sort()
#     minimumChangeCreated = 0
#     for coin in coins:
#         if coin > minimumChangeCreated + 1:
#             return minimumChangeCreated + 1
#         minimumChangeCreated += coin
#     return minimumChangeCreated + 1

