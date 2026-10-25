# O(n) time | O(n)space
def balancedBrackets(string):
    stack = []
    brackets = {"}" : "{", "]":"[", ")":"("}
    openingBrackets ="({["
    closingBrackets = ")}]"
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack or brackets[char] != stack[-1]:
                return False
            stack.pop()        
    return not stack


def isPalindrome(string):
    leftIdx  , rightIdx = 0 , len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True    


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if head is None or head.next is None:
        return head
    currentNode = head
    nextNode = currentNode.next
    currentNode.next = nodeSwap(nextNode.next)
    nextNode.next = currentNode
    return nextNode