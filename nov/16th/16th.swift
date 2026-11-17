// class Program {
//   // This is an input class. Do not edit.
//   class LinkedList {
//     var value: Int
//     var next: LinkedList?

//     init(value: Int) {
//       self.value = value
//     }
//   }

//   func mergeLinkedLists(_ headOne: LinkedList, _ headTwo: LinkedList) -> LinkedList {
//     var nodeOne :LinkedList? = headOne
//     var nodeTwo :LinkedList? = headTwo
//     let node: LinkedList = LinkedList(value: -1)
//     var currentNode = node

//     while nodeOne !== nil && nodeTwo !== nil {
//         var valueOne = nodeOne!.value
//         var valueTwo = nodeTwo!.value

//         if valueOne <= valueTwo {
//             currentNode.next = nodeOne
//             nodeOne = nodeOne?.next
//         }else{
//             currentNode.next = nodeTwo
//             nodeTwo = nodeTwo?.next
//         }
//         currentNode = currentNode.next!
//     }
//     currentNode.next = nodeTwo === nil ? nodeOne  : nodeTwo
//     return node.next! 
//   }
// }


class Program {
  class LinkedList {
    var value: Int
    var next: LinkedList?

    init(value: Int) {
      self.value = value
      next = nil
    }
  }

  static func shiftLinkedList(_ head: LinkedList, _ k: Int) -> LinkedList? {
    var currentNode:LinkedList? = head
    var totalLength = 1
    while currentNode !== nil && currentNode.next !== nil {
        currentNode = currentNode?.next
        totalLength += 1
    }
    var offset = abs(k) % totalLength
    if offset == 0 {
        return head
    }
    var position = k > 0 ? totalLength - offset : offset
    var newTailNode = head
    for _ in 1..<position {
        newTailNode = newTailNode!.next
    }
    newHead = newTailNode!.next
    newTailNode!.next = nil
    currentNode.next = head
    return newHead
  }
}
