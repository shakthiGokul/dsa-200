# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slowNode = head
    fastNode = head.next

    while fastNode is not None and fastNode.next is not None and slowNode != fastNode:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    fastNode = head

    while fastNode is not None and slowNode is not None and slowNode == fastNode:
        slowNode = slowNode.next
        fastNode = fastNode.next
    return slowNode        

