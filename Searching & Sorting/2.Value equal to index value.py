arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
def index_ele(arr):
    start = 0
    end = len(arr) - 1
    while start<=end:
        mid = start + (end - start) // 2
        if arr[mid]==mid:
            return (mid)
        elif arr[mid]<mid:
            start=mid+1
        else:
            end=mid-1
print(index_ele(arr))
