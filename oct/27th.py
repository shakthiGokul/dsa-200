def reversePolishNotation(tokens):
    stack = []
    operators = {'+': 'add' , '-': 'subtract' , '*': 'multiplication' , '/':'division'}
    for char in tokens:
        if char not in operators:
            stack.append(int(char))
        else:
                numberOne = stack.pop()
                numberTwo = stack.pop()
                results = 0
                if operators[char] == 'add':
                    results = numberOne + numberTwo
                elif operators[char] == 'subtract':
                    results = numberTwo - numberOne
                elif operators[char] == 'multiplication':
                    results = numberTwo * numberOne
                else:
                    results = numberTwo / numberOne
                stack.append(int(results))                 
    return stack.pop()

INCREASING = 'INCREASING'
DECREASING = 'DECREASING'
def isMonotonic(array):
    if len(array) <= 1:
        return True
    updatedIdx = 1
    for idx in range(1,len(array)):
        if array[idx] != array[idx - 1]:
            array[updatedIdx] = array[idx]
            updatedIdx += 1
    direction = INCREASING  if array[1] > array[0] else DECREASING
    currentDirection = direction
    for idx in range(1 , updatedIdx):
        numberOne = array[idx]
        numberTwo = array[idx - 1]
        currentDirection =INCREASING  if numberOne > numberTwo else DECREASING
        if currentDirection != direction:
            return False
    return True    
