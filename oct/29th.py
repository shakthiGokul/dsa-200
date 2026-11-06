def runLengthEncoding(string):
    encodedLength = []
    count = 1
    currentChar = string[0]
    for idx in range(1, len(string)):
        char = string[idx]
        if count == 9 or char != currentChar:
            encodedLength.append(str(count))
            encodedLength.append(currentChar)
            count = 0
            currentChar = char
        if char == currentChar:
            count += 1    
    if count > 0:
        encodedLength.append(str(count))
        encodedLength.append(currentChar)          
    return "".join(encodedLength)

# O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    for i in range(len(buildings)):
        minBuildingHeight = buildings[i]
        for j in range(i , len(buildings)):
            minBuildingHeight = min(minBuildingHeight , buildings[j])
            currentArea = minBuildingHeight * ((j  - i ) + 1)
            maxArea = max(maxArea , currentArea)

    return maxArea