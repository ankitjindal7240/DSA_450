def heapify(arr,n,i):
    largest=i #root
    l=2*i +1    #left
    r=2*i +2    #right
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i: # if root is not largest
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def buidHeap(arr):
    n=len(arr)
    start=n//2 -1
    for i in range(start,-1,-1):
        heapify(arr,n,i)

def deleteRoot(arr):
    n=len(arr)
    last=arr[-1]
    arr[0]=last
    arr.pop()
    heapify(arr,n,0)
    print(arr)


def insertElem(arr,key):
    arr.append(key)
    key_index=len(arr)-1
    parent=(key_index+1)//2 -1
    while parent>=0 and arr[parent]<arr[key_index]:
        arr[parent] , arr[key_index]=arr[key_index],arr[parent]
        key_index=parent
        parent=(key_index+1)//2 -1
# Driver Code
if __name__ == '__main__':
    arr=[1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17]
    buidHeap(arr)
    print(arr)
    deleteRoot(arr)
    print(arr)
    insertElem(arr,17)
    print(arr)