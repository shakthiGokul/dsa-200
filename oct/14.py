# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    fastNode = head
    counter = 1
    while counter <= k and fastNode:
        fastNode = fastNode.next
        counter += 1
    if fastNode is None:
        head.value = head.next.value
        head.next = head.next.next
        return    
    slowNode = head
    while fastNode is not None and fastNode.next is not None:
        fastNode = fastNode.next
        slowNode = slowNode.next
    slowNode.next = slowNode.next.next
    return head     