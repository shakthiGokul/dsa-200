class Program {
  // This is an input class. Do not edit.
  class LinkedList {
    var value: Int
    var next: LinkedList?

    init(value: Int) {
      self.value = value
    }
  }

  func sumOfLinkedLists(_ linkedListOne: LinkedList, _ linkedListTwo: LinkedList) -> LinkedList? {
    var nodeOne: LinkedList? = linkedListOne
    var nodeTwo: LinkedList? = linkedListTwo
    let node = LinkedList(value: -1)
    var currentNode = node
    var carry = 0
    
    while nodeOne != nil || nodeTwo != nil || carry != 0 {
      let numberOne = nodeOne?.value ?? 0
      let numberTwo = nodeTwo?.value ?? 0
      
      let currentSum = numberOne + numberTwo + carry
      let currentDigit = currentSum % 10
      carry = currentSum / 10
      
      let newNode = LinkedList(value: currentDigit)
      currentNode.next = newNode
      currentNode = newNode
      
      nodeOne = nodeOne?.next
      nodeTwo = nodeTwo?.next
    } 
    
    return node.next
  }
}
