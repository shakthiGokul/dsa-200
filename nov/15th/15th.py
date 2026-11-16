# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slowNode , fastNode = head.next , head.next.next
    while fastNode != slowNode:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    fastNode = head
    while fastNode != slowNode:
        fastNode = fastNode.next
        slowNode = slowNode.next
    return slowNode    
