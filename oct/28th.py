def collidingAsteroids(asteroids):
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
            continue

        while True:
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
                break
            currentAsteroid = abs(asteroid)
            if stack[-1] > currentAsteroid:
                break
            if stack[-1] == currentAsteroid or  stack[-1] < currentAsteroid:
                stack.pop()
                break    
    return stack

def shortenPath(path):
    startWithSlash = path[0] == '/'
    tokens = filter(getTokens, path.split("/"))
    stack = []
    if startWithSlash:
        stack.append("")
    for token in tokens:
        if token != "..":
            stack.append(token)
            continue
        if len(stack) == 0 or stack[-1] == "..":
            stack.append(token)
        elif stack[-1] != "":
            stack.pop()    
    return "/" if stack == [""] else "/".join(stack)
def getTokens(token):
    return token != '.' and token != ""