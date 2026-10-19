# #  This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # def sumOfLinkedLists(linkedListOne, linkedListTwo):
# #     node = LinkedList(-1)
# #     currentNode = node
# #     nodeOne = linkedListOne
# #     nodeTwo = linkedListTwo
# #     carry = 0 
# #     while nodeOne is not None or nodeTwo is not None or carry !=0:
# #         valueOne = nodeOne.value if nodeOne is not None else 0
# #         valueTwo = nodeTwo.value if nodeTwo is not None else 0
# #         sumOfValue = valueOne + valueTwo + carry
# #         carry = sumOfValue // 10
# #         digit = sumOfValue % 10
# #         if currentNode:
# #             currentNode.next = LinkedList(digit)
# #             currentNode = currentNode.next
# #         nodeOne = nodeOne.next if nodeOne is not None else None
# #         nodeTwo = nodeTwo.next if nodeTwo is not None else None
# #     return node.next

# # This is an input class. Do not edit.
# # class LinkedList:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None

# # # O(n + m) time | O(n) space
# # def mergingLinkedLists(linkedListOne, linkedListTwo):
# #     nodeOne = linkedListOne
# #     nodes = set()
# #     while nodeOne is not None:
# #         nodes.add(nodeOne)
# #         nodeOne = nodeOne.next
# #     nodeTwo = linkedListTwo
# #     while nodeTwo is not None:
# #         if nodeTwo in nodes:
# #             break
# #         nodeTwo = nodeTwo.next    
# #     return nodeTwo


# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# # O(n + m) time | O(1) space 
# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     nodeOne = linkedListOne
#     nodeTwo = linkedListTwo
#     while nodeOne !=nodeTwo:
#         nodeOne = nodeOne.next if nodeOne is not None else linkedListTwo
#         nodeTwo = nodeTwo.next if nodeTwo is not None else linkedListOne
#     return nodeOne

# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     nodeOne = linkedListOne
#     nodeTwo = linkedListTwo
#     while True:
#         if nodeOne is nodeTwo:
#             break
#         nodeOne = nodeOne.next if nodeOne is not None else linkedListTwo
#         nodeTwo = nodeTwo.next if nodeTwo is not None else linkedListOne
#     return nodeOne

# O(n ^ 3) time | O(n) space
# def longestPalindromicSubstring(string):
#     bounds = [0 , 0]
#     for i in range(len(string)):
#         for j in range(len(string)):
#            if isPalindrome(string , i , j):
#                if bounds[1] - bounds[0] < j - i:
#                    bounds = [i , j]
#     return string[bounds[0]: bounds[1] + 1]

def longestPalindromicSubstring(string):
    bounds = [0 , 1]

    for i in range(1,len(string)):
        oddLength = getLongestPalindromeFrom(string , i - 1 , i + 1)
        evenLength = getLongestPalindromeFrom(string , i - 1, i)
        longest = max(oddLength , evenLength , key=lambda x:x[1] - x[0])
        bounds = max(longest, bounds, key=lambda x:x[1] - x[0])
    return string[bounds[0]: bounds[1]]          

def getLongestPalindromeFrom(string , leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string) and string[leftIdx] == string[rightIdx]:
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1 , rightIdx]  