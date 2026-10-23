# O(n) time | O(n)space
def balancedBrackets(string):
    stack = []
    brackets = {"}" : "{", "]":"[", ")":"("}
    openingBrackets ="({["
    closingBrackets = ")}]"
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack or brackets[char] != stack[-1]:
                return False
            stack.pop()        
    return not stack              