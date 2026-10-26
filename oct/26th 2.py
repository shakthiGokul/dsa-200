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