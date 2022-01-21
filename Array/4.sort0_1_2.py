arr=[0,0,1,2,2,1,0,1,1,2,2,0,0]
low=0
mid=0
high=len(arr)-1
while mid<=high:
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        low=low+1
    if arr[mid]==2:
        arr[mid], arr[high] = arr[high], arr[mid]
        high=high-1
    else:
        mid=mid+1
print(arr)
