arr = [-1, 2,0, -3, 4, 5,0, 6, -7, 8, 9]
left=0
righ=len(arr)-1
while righ>left:
    if arr[left]<0:
        left=left+1
    if arr[righ]>0:
        righ=righ-1
    if arr[left]>0 and arr[righ]<0:
        arr[left],arr[righ]=arr[righ],arr[left]

print(arr)
