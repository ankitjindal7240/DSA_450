arr=[1,4,5,7,2,4,9,21,12,45,67,87,34,]

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>0 and arr[j]>key  :
        arr[j+1] =arr[j]
        j=j-1
    arr[j+1]=key

print(arr)