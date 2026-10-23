# def sunsetViews(buildings, direction):
#     if not buildings:
#         return []
#     stack = []
#     if direction == 'EAST':
#         stack.append(len(buildings) - 1)
#         for idx in reversed(range(0, len(buildings) - 1)):
#            lastHeight = buildings[stack[-1]]
#            if lastHeight < buildings[idx]:
#                stack.append(idx)
#     else:
#         stack.append(0)
#         for idx in range(1, len(buildings)):
#             lastHeight = buildings[stack[-1]]
#             if lastHeight < buildings[idx]:
#                 stack.append(idx)               
#     return stack[::-1] if direction == 'EAST' else stack      

# def sunsetViews(buildings, direction):
#     n = len(buildings)
#     if direction == 'EAST':
#         start, end, step = n - 1, -1, -1
#     else:
#         start, end, step = 0, n, 1

#     stack = []
#     maxHeight = float('-inf')
#     for idx in range(start, end, step):
#         if buildings[idx] > maxHeight:
#             stack.append(idx)
#             maxHeight = buildings[idx]
#     return stack[::-1] if direction == 'EAST' else stack

    
               