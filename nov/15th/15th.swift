class Program {
  // This is an input class. Do not edit.
  class LinkedList {
    var value: Int
    var next: LinkedList?

    init(value: Int) {
      self.value = value
      next = nil
    }
  }

  func findLoop(head: LinkedList) -> LinkedList? {
    var slowNode : LinkedList? = head?.next
    var fastNode :LinkedList? = head?.next?.next

    while slowNode !== fastNode {
        slowNode = slowNode?.next
        fastNode = fastNode?.next?.next
    }
    fastNode = head

    while slowNode !== fastNode {
        slowNode = slowNode?.next
        fastNode = fastNode?.next
    }
    return slowNode
  }
}