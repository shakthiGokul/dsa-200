# def reversePolishNotation(tokens):
#     stack = []
#     operators = {'+': 'add' , '-': 'subtract' , '*': 'multiplication' , '/':'division'}
#     for char in tokens:
#         if char not in operators:
#             stack.append(int(char))
#         else:
#                 numberOne = stack.pop()
#                 numberTwo = stack.pop()
#                 results = 0
#                 if operators[char] == 'add':
#                     results = numberOne + numberTwo
#                 elif operators[char] == 'subtract':
#                     results = numberTwo - numberOne
#                 elif operators[char] == 'multiplication':
#                     results = numberTwo * numberOne
#                 else:
#                     results = numberTwo / numberOne
#                 stack.append(int(results))                 
#     return stack.pop()

# INCREASE = 'INCREASE'
# DECREASE = 'DECREASE'
# FLAT_LINE =' FLAT_LINE'
# def isMonotonic(array):
#     if len(array) <= 1:
#         return True
#     updatedIdx = 1
#     for idx in range(1,len(array)):
#         if array[idx] != array[idx - 1]:
#             array[updatedIdx] = array[idx]
#             updatedIdx += 1
#     direction = INCREASE  if array[1] > array[0] else DECREASE
#     currentDirection = direction
#     for idx in range(1 , updatedIdx):
#         numberOne = array[idx]
#         numberTwo = array[idx - 1]
#         currentDirection =INCREASE  if numberOne > numberTwo else DECREASE
#         if currentDirection != direction:
#             return False
#     return True    

# def isMonotonic(array):
#     if len(array) <= 1:
#         return True
#     direction = FLAT_LINE
#     currentDirection = direction
#     for idx in range(1, len(array)):
#         prevNumber = array[idx -1]
#         currentNumber = array[idx]
#         if currentNumber == prevNumber:
#             continue
#         elif currentNumber > prevNumber:
#             currentDirection = INCREASE
#         else:
#             currentDirection = DECREASE
#         if currentDirection is not FLAT_LINE and direction is FLAT_LINE:
#             direction = currentDirection        
#         if currentDirection != FLAT_LINE and currentDirection != direction:
#             return False
#     return True
