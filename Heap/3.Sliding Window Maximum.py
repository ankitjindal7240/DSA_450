arr = [12, 1, 78, 90, 57, 89, 56]
k=3
lst=[]
i=0
j=0
ans=[]
while (j-i+1)<=k:
    while len(lst)>0 and lst[-1]<arr[j]:
        lst.pop()
    lst.append(arr[j])
    j=j+1
while j<len(arr):
    ans.append(lst[0])
    if arr[i]==lst[0]:
        lst.pop(0)
    i=i+1
    while len(lst)>0 and lst[-1]<arr[j]:
        lst.pop()
    lst.append(arr[j])
    j=j+1
ans.append(lst[0])
print(ans)



