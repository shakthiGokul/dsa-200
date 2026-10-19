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
#     slowNode = fastNode = linkedList
#     while fastNode is not None and fastNode.next is not None:
#         slowNode = slowNode.next
#         fastNode = fastNode.next.next
#     return slowNode

# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     nums = set()
#     for num in array:
#         currentNum = targetSum - num
#         if currentNum in nums:
#             return [currentNum , num]
#         nums.add(num)
#     return []    