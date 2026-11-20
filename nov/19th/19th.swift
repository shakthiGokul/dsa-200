class Program {
  // This is an input class. Do not edit.
  class LinkedList {
    var value: Int
    var next: LinkedList?

    init(value: Int) {
      self.value = value
    }
  }

  func linkedListPalindrome(_ head: LinkedList) -> Bool {
    if head.next == nil { return true }
    var slowNode:LinkedList = head
    var fastNode:LinkedList? = head.next

    while fastNode !== nil && fastNode!.next !== nil {
        fastNode = fastNode!.next!.next
        slowNode = slowNode.next!
    }
    var nodeOne:LinkedList? = reverseLinkedList(slowNode.next!)
    slowNode.next = nil
    var nodeTwo:LinkedList? = head

    while nodeOne !== nil && nodeTwo !== nil {
        if nodeOne!.value != nodeTwo!.value {
            return false
        }
        nodeOne = nodeOne?.next
        nodeTwo = nodeTwo?.next
    }
    return true
  }
  func reverseLinkedList(_ head:LinkedList) -> LinkedList {
    var currentNode:LinkedList? = head
    var prevNode:LinkedList? = nil

    while currentNode !== nil {
        let nextNode = currentNode!.next
        currentNode!.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    }
    return prevNode!
  }
}