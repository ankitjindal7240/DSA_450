def binarySearch(arr,start,end,key):
    if start>end:
        return False
    mid = start + (end-start)//2
    if arr[mid] ==key:
        return True
    elif arr[mid]<key:
        return binarySearch(arr,mid+1,end,key)
    else:
        return binarySearch(arr,start,mid-1,key)

def matrixSearch(matrix,start,end,key):
    if start>end:
        return False
    mid = start + (end - start) // 2
    if matrix[mid][0] ==key:
        return True
    elif matrix[mid][0] > key:
        return matrixSearch(matrix,start, mid - 1, key)
    else:
        if key<=matrix[mid][-1]:
            return binarySearch(matrix[mid],0,len(matrix[0])-1,key)
        else:
            return matrixSearch(matrix,mid+1,end,key)


matrix = [[1,3,5,7]
        ,[10,11,16,20]
        ,[23,30,34,60]]
matrix=[[1,3]]
print(binarySearch(matrix[0],0,len(matrix[0])-1,3))
print(matrixSearch(matrix,0,len(matrix)-1,3))