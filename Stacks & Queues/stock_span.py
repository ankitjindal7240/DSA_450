arr=[100,80,85,90,95,60,70]
def next_greater_left(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)):  #*
        if len(stack)==0:
            ans.append(i-1)
        elif arr[stack[-1]] >=arr[i]:
            ans.append(i-stack[-1])

        else:
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(i--1)
            elif arr[stack[-1]]>=arr[i]:
                ans.append(i-stack[-1])
        stack.append(i)

    # ans.reverse()
    print(ans)

    return ans
next_greater_left(arr)
