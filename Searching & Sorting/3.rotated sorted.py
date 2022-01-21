def binarysearch(arr,l,r,key):
    if l>r:
        return -1
    mid=l+(r-l)//2
    if arr[mid]==key:
        return mid
    if arr[l]<=arr[mid]:
        if arr[mid]>=key:
            return binarysearch(arr,l,mid,key)
        return binarysearch(arr, mid, r, key)
    else:
        if arr[mid]<=key:
            return binarysearch(arr,mid, r,key)
        return binarysearch(arr, l,mid, key)