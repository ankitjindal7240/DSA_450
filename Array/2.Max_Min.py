arr=[3,5,99,24,21,33,98,45,32,56,43,0,2]
# 1. simple approach
mn=0
mx=0
for i in range(len(arr)):
    if arr[i]>mx:
        mx=arr[i]
    elif arr[i]<mn:
        mn=arr[i]

# 2. optimised
l=len(arr)
if l%2==0:
    if arr[0]<arr[1]:
        mn=arr[0]
        mx=arr[1]
    else:
        mn = arr[1]
        mx = arr[0]
    i=2
else:
    mn=arr[0]
    mx=arr[0]
    i=1
while i<len(arr)-1:

    if arr[i]>arr[i+1]:
        mx=max(arr[i],mx)
        mn=min(arr[i+1],mn)
    else:
        mx = max(arr[i+1], mx)
        mn = min(arr[i],mn)
    i=i+2
print(mn,mx)