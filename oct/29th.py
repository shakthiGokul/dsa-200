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