s = ")("
def isParentheses(s):
    return s=="(" or s==")"
def isValidString(s):
    count=0
    for i in range(len(s)):
        if s[i]=="(":
            count=count+1
        elif s[i]==")":
            count=count-1
        if count<0:
            return False
    return count==0
def removeParentheses(s):
    if len(s)==0:
        return
    if isValidString(s):
        print(s)
        return
    visited=set()
    level=0
    q=[]
    q.append(s)
    visited.add(s)
    while q:
        s=q.pop(0)
        if isValidString(s):
            print(s)
            level=True
        if level:
            continue
        for i in range(len(s)):
            # print(i)
            if isParentheses(s[i]):
                temp=s[:i] + s[i+1:]     # special check of i+1
                # print(temp)
                if temp not in visited:
                    q.append(temp)
                    visited.add(temp)

removeParentheses(s)
