// // class Program {
// //   // This is an input class. Do not edit.
// //   class LinkedList {
// //     var value: Int
// //     var next: LinkedList?

// //     init(value: Int) {
// //       self.value = value
// //     }
// //   }

// //   func linkedListPalindrome(_ head: LinkedList) -> Bool {
// //     if head.next == nil { return true }
// //     var slowNode:LinkedList = head
// //     var fastNode:LinkedList? = head.next

// //     while fastNode !== nil && fastNode!.next !== nil {
// //         fastNode = fastNode!.next!.next
// //         slowNode = slowNode.next!
// //     }
// //     var nodeOne:LinkedList? = reverseLinkedList(slowNode.next!)
// //     slowNode.next = nil
// //     var nodeTwo:LinkedList? = head

// //     while nodeOne !== nil && nodeTwo !== nil {
// //         if nodeOne!.value != nodeTwo!.value {
// //             return false
// //         }
// //         nodeOne = nodeOne?.next
// //         nodeTwo = nodeTwo?.next
// //     }
// //     return true
// //   }
// //   func reverseLinkedList(_ head:LinkedList) -> LinkedList {
// //     var currentNode:LinkedList? = head
// //     var prevNode:LinkedList? = nil

// //     while currentNode !== nil {
// //         let nextNode = currentNode!.next
// //         currentNode!.next = prevNode
// //         prevNode = currentNode
// //         currentNode = nextNode
// //     }
// //     return prevNode!
// //   }
// // }

// class Program {
//   // This is an input class. Do not edit.
//   class LinkedList {
//     var value: Int
//     var next: LinkedList?

//     init(value: Int) {
//       self.value = value
//     }
//   }

//   func zipLinkedList(_ linkedList: LinkedList) -> LinkedList {
//     // 1. Handle edge cases: lists with 1 or 2 nodes are already zipped
//     if linkedList.next == nil || linkedList.next?.next == nil {
//       return linkedList
//     }

//     // 2. Find the midpoint of the linked list
//     var slowNode: LinkedList? = linkedList
//     var fastNode: LinkedList? = linkedList.next
//     while fastNode !== nil && fastNode?.next !== nil {
//       slowNode = slowNode?.next
//       fastNode = fastNode?.next?.next
//     }

//     // 3. Split the list and reverse the second half
//     let secondHalfHead = slowNode!.next!
//     slowNode!.next = nil
    
//     var currentNodeOne: LinkedList? = linkedList
//     var currentNodeTwo: LinkedList? = reverseLinkedList(secondHalfHead)

//     // 4. Interweave (zip) the two halves together
//     while currentNodeOne !== nil && currentNodeTwo !== nil {
//       let nextNodeOne = currentNodeOne?.next
//       let nextNodeTwo = currentNodeTwo?.next

//       currentNodeOne?.next = currentNodeTwo
//       currentNodeTwo?.next = nextNodeOne

//       currentNodeOne = nextNodeOne
//       currentNodeTwo = nextNodeTwo
//     }

//     // 5. Return the original head of the list
//     return linkedList
//   }

//   func reverseLinkedList(_ head: LinkedList) -> LinkedList {
//     var currentNode: LinkedList? = head
//     var prevNode: LinkedList? = nil

//     while currentNode !== nil {
//       let nextNode = currentNode!.next
//       currentNode!.next = prevNode
//       prevNode = currentNode
//       currentNode = nextNode
//     }
//     return prevNode!
//   }
// }

class Program {
  func nonConstructibleChange(_ coins: inout [Int]) -> Int {
    var currentChangedCreated = 0
    var sortedCoins = coins.sorted()
    for coin in sortedCoins {
      if coin > currentChangedCreated + 1{
        return currentChangedCreated + 1
      }
      currentChangedCreated += coin
    }
    return currentChangedCreated + 1
  }
}

