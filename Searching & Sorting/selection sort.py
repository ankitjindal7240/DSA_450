arr=[1,4,5,7,2,4,9,21,12,45,67,87,34,]

for i in range(len(arr)):
    min_inddex=i
    for j in range(i,len(arr)):
        if arr[j]<arr[min_inddex]:
            min_inddex=j
    arr[i],arr[min_inddex]=arr[min_inddex],arr[i]
print(arr)