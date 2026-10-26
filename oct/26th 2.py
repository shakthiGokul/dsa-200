class MinMaxStack:
    def __init__(self) -> None:
       self.minMaxStack = []
       self.stack = []
    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        stack = self.stack
        minMaxStack = self.minMaxStack
        newMinMaxStack = {'min': number , 'max': number}
        if stack:
            currentMinMaxStack = minMaxStack[-1]
            currentMin , currentMax = currentMinMaxStack['min'] , currentMinMaxStack['max']
            newMinMaxStack['min'] = min(currentMin , number)
            newMinMaxStack['max']  = max(currentMax , number)
        minMaxStack.append(newMinMaxStack)    
        stack.append(number)    


    def getMin(self):
       return self.minMaxStack[-1]['min']

    def getMax(self):
        return self.minMaxStack[-1]['max']


def longestSubarrayWithSum(array, targetSum):
    longest = []
    leftIdx = 0
    currentSum = 0
    for rightIdx in range(len(array)):
        currentSum += array[rightIdx]
        while leftIdx < rightIdx and currentSum > targetSum:
            currentSum -= array[leftIdx]
            leftIdx += 1
        currentLength = rightIdx - leftIdx   
        if currentSum == targetSum:
            if len(longest) == 0 or  currentLength > longest[1] - longest[0]:
                longest = [leftIdx , rightIdx]     
    return longest                       
