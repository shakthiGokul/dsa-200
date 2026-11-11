class Program {
  func largestRectangleUnderSkyline(_ buildings: [Int]) -> Int {
    var maxArea = 0
    for idx in stride(from:0 , to: buildings.count, by:1){
        let currentHeight = buildings[idx]
        var leftBound = idx 
        var rightBound = idx 

        while leftBound > 0 , buildings[leftBound - 1] >= currentHeight{
            leftBound -= 1
        }

        while rightBound < buildings.count - 1 , buildings[rightBound + 1] >= currentHeight{
            rightBound += 1
        }
        let currentMaxHeight = (rightBound - leftBound + 1) * currentHeight
        maxArea = max(currentMaxHeight , maxArea)

    }
    return maxArea
  }
}
