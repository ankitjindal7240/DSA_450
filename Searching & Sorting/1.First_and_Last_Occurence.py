
def firstOccurence(arr,start,end,key):

    while start<=end:
        mid = start + (end - start) // 2
        if arr[mid]>key:
            end=mid-1
        elif arr[mid]<key:
            start=mid+1
        else:
            if mid==0 or arr[mid-1]!=key:
                return mid
            else:
                end=mid-1
def lastOccurence(arr,start,end,key):

    while start<=end:
        mid = start + (end - start) // 2
        if arr[mid]>key:
            end=mid-1
        elif arr[mid]<key:
            start=mid+1
        else:
            if mid==len(arr)-1 or arr[mid+1]!=key:
                return mid
            else:
                start=mid+1

# Driver Code
if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125 ]
    start=0
    end=len(arr)-1
    print(firstOccurence(arr,start,end,1))
    print(lastOccurence(arr,start,end,1))



