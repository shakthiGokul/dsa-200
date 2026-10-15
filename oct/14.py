# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def removeKthNodeFromEnd(head, k):
#     fastNode = head
#     counter = 1
#     while counter <= k and fastNode:
#         fastNode = fastNode.next
#         counter += 1
#     if fastNode is None:
#         head.value = head.next.value
#         head.next = head.next.next
#         return    
#     slowNode = head
#     while fastNode is not None and fastNode.next is not None:
#         fastNode = fastNode.next
#         slowNode = slowNode.next
#     slowNode.next = slowNode.next.next
#     return head

# #O(n + m) time |O(k) space 

# HOME_TEAM = 1 
# def tournamentWinner(competitions, results):
#     scores = {'' : 0}
#     bestTeam = ''
#     for idx in range(len(results)):
#         result = results[idx]
#         [homeTeam , awayTeam] = competitions[idx]
#         winningTeam = homeTeam if result == HOME_TEAM else awayTeam
#         updateScores(scores, winningTeam, 3)
#         if scores[bestTeam] < scores[winningTeam]:
#             bestTeam = winningTeam
#     return bestTeam

# def updateScores(scores, winningTeam , point):
#     if winningTeam in scores:
#         scores[winningTeam] += point
#     else:
#         scores[winningTeam] = point

# This is an input class. Do not edit.

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head , node)    

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail , node)
        
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert    
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.tail and nodeToInsert == self.head:
            self.setTail(nodeToInsert)
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:    
            node.next.prev = nodeToInsert
        node.next = nodeToInsert   
        

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            return self.setHead(nodeToInsert)
        counter = 1
        currentNode = self.head
        while currentNode is not None and counter != position:
            counter += 1
            currentNode = currentNode.next
        self.setTail(nodeToInsert) if currentNode is None else self.insertBefore(currentNode , nodeToInsert) 

    def removeNodesWithValue(self, value):
        currentNode = self.head
        while currentNode is not None:
            nodeToRemove = currentNode
            currentNode = currentNode.next
            if value == nodeToRemove.value:
                self.remove(nodeToRemove)
               
    def remove(self, node):
        if self.head is None or self.tail is None:
            return
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev    
        self.removeNodeBindings(node)   
       
    def containsNodeWithValue(self, value):
        currentNode = self.head
        while currentNode is not None:
            if value == currentNode.value:
                return True
            currentNode = currentNode.next
        return False

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev  
        node.prev = None
        node.next = None     
           
        