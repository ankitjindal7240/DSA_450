stack=[5,9,2,8,6]
n=len(stack)
mid=n//2
def solve(stack,mid):
    if mid ==0:
        stack.pop()
        return
    p=stack.pop()
    solve(stack,mid-1)
    stack.append(p)
solve(stack,mid)
print(stack)