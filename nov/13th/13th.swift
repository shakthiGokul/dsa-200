// // // // class Program {
// // // //   // This is an input class. Do not edit.
// // // //   class LinkedList {
// // // //     var value: Int
// // // //     var next: LinkedList?

// // // //     init(value: Int) {
// // // //       self.value = value
// // // //     }
// // // //   }

// // // //   func sumOfLinkedLists(_ linkedListOne: LinkedList, _ linkedListTwo: LinkedList) -> LinkedList? {
// // // //     var nodeOne: LinkedList? = linkedListOne
// // // //     var nodeTwo: LinkedList? = linkedListTwo
// // // //     let node = LinkedList(value: -1)
// // // //     var currentNode = node
// // // //     var carry = 0
    
// // // //     while nodeOne != nil || nodeTwo != nil || carry != 0 {
// // // //       let numberOne = nodeOne?.value ?? 0
// // // //       let numberTwo = nodeTwo?.value ?? 0
      
// // // //       let currentSum = numberOne + numberTwo + carry
// // // //       let currentDigit = currentSum % 10
// // // //       carry = currentSum / 10
      
// // // //       let newNode = LinkedList(value: currentDigit)
// // // //       currentNode.next = newNode
// // // //       currentNode = newNode
      
// // // //       nodeOne = nodeOne?.next
// // // //       nodeTwo = nodeTwo?.next
// // // //     } 
    
// // // //     return node.next
// // // //   }
// // // // }

// // // class Program {
// // //   // This is an input class. Do not edit.
// // //   class LinkedList: Hashable {
// // //     var value: Int
// // //     var next: LinkedList?

// // //     init(value: Int) {
// // //       self.value = value
// // //     }

// // //     func hash(into hasher: inout Hasher) {
// // //       hasher.combine(ObjectIdentifier(self).hashValue)
// // //     }

// // //     static func == (left: LinkedList, right: LinkedList) -> Bool {
// // //       return left === right
// // //     }
// // //   }

// // //   func mergingLinkedLists(_ linkedListOne: LinkedList, _ linkedListTwo: LinkedList) -> LinkedList? {
// // //     var nodeOne:LinkedList? = linkedListOne
// // //     var nodeTwo:LinkedList? = linkedListTwo
// // //     var visitedNodes = Set<LinkedList>()
// // //     while nodeOne != nil {
// // //         visitedNodes.insert(nodeOne!)
// // //         nodeOne = nodeOne!.next
// // //     }
// // //     while nodeTwo != nil {
// // //         if visitedNodes.contains(nodeTwo!) {
// // //             return nodeTwo
// // //         }
// // //         nodeTwo = nodeTwo!.next
// // //     }
// // //     return nil
// // //   }
// // // }

// // class Program {
// //   // This is an input class. Do not edit.
// //   class LinkedList: Hashable {
// //     var value: Int
// //     var next: LinkedList?

// //     init(value: Int) {
// //       self.value = value
// //     }

// //     func hash(into hasher: inout Hasher) {
// //       hasher.combine(ObjectIdentifier(self).hashValue)
// //     }

// //     static func == (left: LinkedList, right: LinkedList) -> Bool {
// //       return left === right
// //     }
// //   }

// //   func mergingLinkedLists(_ linkedListOne: LinkedList, _ linkedListTwo: LinkedList) -> LinkedList? {
// //     var nodeOne:LinkedList? = linkedListOne
// //     var nodeTwo:LinkedList? = linkedListTwo
// //     while nodeOne != nil || nodeTwo != nil{
// //         if nodeOne == nodeTwo {
// //             return nodeOne
// //         }
// //         nodeOne = nodeOne != nil ? nodeOne!.next : linkedListTwo
// //         nodeTwo = nodeTwo != nil ? nodeTwo!.next : linkedListOne
// //     }
// //     return nil
// //   }
// // }

// class Program {
//   func isPalindrome(string: String) -> Bool {
//     var leftBound = 0
//     var rightBound = string.count - 1
//     var leftIdx = string.index(string.startIndex , offsetBy: leftBound)
//     var rightIdx = string.index(string.startIndex , offsetBy: rightBound)
//     while leftIdx < rightIdx {
//         if string[leftIdx] != string[rightIdx] {
//             return false
//         }
//         leftBound += 1
//         rightBound -= 1
//         leftIdx = string.index(string.startIndex , offsetBy: leftBound)
//         rightIdx = string.index(string.startIndex , offsetBy: rightBound)
//     }
//     return true
//   }
// }
