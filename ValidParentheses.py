def isValid(s):
    stack = []
    myMap = {")": "(", "]": "[", "}": "{"}

    for element in s:
        if element in myMap:
            if stack and stack[-1] == myMap[element]:
                stack.pop()
            else:
                return False
        else:
            stack.append(element)
    return True if not stack else False
