arr=[5,3,2,4,9,6,12,56,1,7,22,43,78]
k=3
# 1. brute force
def kthSmallest(arr,k):
    for i in range(k):
        for j in range(1,len(arr)-i):
            if arr[j-1]<arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr[-k]

