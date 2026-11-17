class Program {
  // This is an input class. Do not edit.
  class LinkedList {
    var value: Int
    var next: LinkedList?

    init(value: Int) {
      self.value = value
    }
  }

  func mergeLinkedLists(_ headOne: LinkedList, _ headTwo: LinkedList) -> LinkedList {
    var nodeOne :LinkedList? = headOne
    var nodeTwo :LinkedList? = headTwo
    let node: LinkedList = LinkedList(value: -1)
    var currentNode = node

    while nodeOne !== nil && nodeTwo !== nil {
        var valueOne = nodeOne!.value
        var valueTwo = nodeTwo!.value

        if valueOne <= valueTwo {
            currentNode.next = nodeOne
            nodeOne = nodeOne?.next
        }else{
            currentNode.next = nodeTwo
            nodeTwo = nodeTwo?.next
        }
        currentNode = currentNode.next!
    }
    currentNode.next = nodeTwo === nil ? nodeOne  : nodeTwo
    return node.next! 
  }
}