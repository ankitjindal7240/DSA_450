p={([])}
def parenthesisChecker(p):
    stack=[]
    for i in range(p):
        if p[i]==("{"or"("or"["):
            stack.append([p[i]])
        char=p[i]
        if len(stack) == 0:
            return False
        if char == '}':
            if stack[-1] == '{':
                stack.pop()
                continue
        if char == ')':
            if stack[-1] == '(':
                stack.pop()
                continue
        if char == ']':
            if stack[-1] == '[':
                stack.pop()
                continue
    if len(stack):
        return False
    return True