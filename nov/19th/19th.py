# # # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def linkedListPalindrome(head):
# #     slowNode , fastNode = head , head.next
# #     while fastNode is not None and fastNode.next is not None:
# #         slowNode = slowNode.next
# #         fastNode = fastNode.next.next
# #     nodeOne = reverseLinkedList(slowNode.next)
# #     slowNode.next = None
# #     nodeTwo = head

# #     while nodeOne is not None and nodeTwo is not None:
# #         if nodeOne.value != nodeTwo.value:
# #             return False
# #         nodeOne = nodeOne.next
# #         nodeTwo = nodeTwo.next    
# #     return True

# # def reverseLinkedList(head):
# #     currentNode = head
# #     prevNode = None
# #     while currentNode is not None:
# #         nextNode = currentNode.next
# #         currentNode.next = prevNode
# #         prevNode = currentNode
# #         currentNode = nextNode
# #     return prevNode

# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def zipLinkedList(linkedList):
#     slowNode , fastNode = linkedList , linkedList.next

#     while fastNode is not None and fastNode.next is not None:
#         fastNode = fastNode.next.next
#         slowNode = slowNode.next
#     nodeTwo = reverseLinkedList(slowNode.next)
#     slowNode.next = None
#     nodeOne = linkedList

#     currentNodeOne = nodeOne
#     currentNodeTwo = nodeTwo

#     while currentNodeTwo is not None and currentNodeOne is not None:
#         nextOneNode = currentNodeOne.next
#         nextTwoNode = currentNodeTwo.next

#         currentNodeOne.next = currentNodeTwo
#         currentNodeTwo.next = nextOneNode
#         currentNodeOne = nextOneNode
#         currentNodeTwo = nextTwoNode

#     if currentNodeOne is None:
#         currentNodeOne = currentNodeTwo      
        
#     return  nodeOne

# def reverseLinkedList(head):
#     currentNode = head
#     prevNode = None
#     while currentNode is not None:
#         nextNode = currentNode.next
#         currentNode.next = prevNode
#         prevNode = currentNode
#         currentNode = nextNode
#     return prevNode    

def nonConstructibleChange(coins):
    currentChangeCreated = 0
    coins.sort()
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin    
    return currentChangeCreated + 1  