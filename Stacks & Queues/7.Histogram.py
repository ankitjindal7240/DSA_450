arr=[6,2,5,4,5,1,6]
# next greater element to right
def next_greater_right(arr):
    ans=[]
    stack=[]
    for i in reversed(range(len(arr))): #*
        if len(stack)==0:
            ans.append(-1)
        elif arr[stack[-1]] >arr[i]:
            ans.append(stack[-1])

        else:
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            elif arr[stack[-1]]>arr[i]:
                ans.append(stack[-1])
        stack.append(i)

    ans.reverse()
    print(ans)

    return ans
next_greater_right(arr)
# next greater element to left
def next_greater_left(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)):  #*
        if len(stack)==0:
            ans.append(-1)
        elif arr[stack[-1]] >arr[i]:
            ans.append(stack[-1])

        else:
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            elif arr[stack[-1]]>arr[i]:
                ans.append(stack[-1])
        stack.append(i)

    # ans.reverse()
    print(ans)

    return ans
next_greater_left(arr)
# next smaller to left

def next_smaller_left(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)):  #*
        if len(stack)==0:
            ans.append(-1)
        elif arr[stack[-1]] <arr[i]:
            ans.append(stack[-1])

        else:
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            elif arr[stack[-1]]<arr[i]:
                ans.append(stack[-1])
        stack.append(i)

    # ans.reverse()
    print(ans)

    return ans
next_smaller_left(arr)

# next smaller to right

def next_smaller_right(arr):
    ans=[]
    stack=[]
    for i in reversed(range(len(arr))):  #*
        if len(stack)==0:
            ans.append(-1)
        elif arr[stack[-1]] <arr[i]:
            ans.append(stack[-1])

        else:
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            elif arr[stack[-1]]<arr[i]:
                ans.append(stack[-1])
        stack.append(i)

    ans.reverse()
    print(ans)

    return ans
next_smaller_right(arr)

# largest area histogram
def histogram(arr):
    sm_right=next_smaller_right(arr)
    sm_left=next_smaller_left(arr)
    width=[]
    mx=0
    for i in range(len(arr)):
        width.append(sm_right[i]-sm_left[i]-1)
        area=arr[i]*width[i]
        if area>mx:
            mx=area
    print(mx)
    return mx
histogram(arr)

# important note
"""
in NGR rather than storing -1 store len(arr)
"""