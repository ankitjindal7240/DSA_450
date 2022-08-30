import sys
arr=[30,40,50,30,20,10,60]
mn= sys.maxsize
def solve(arr,i,j):
    global mn
    if i>=j:
        return 0
    for k in range(i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j) + arr[i]*arr[k]*arr[j]
        if temp<mn:
            mn=temp
    return temp
solve(arr,1,len(arr)-1)
print(mn)  