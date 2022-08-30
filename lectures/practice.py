a=[4,2,5,1,6,8,1]
n=len(a)
odd=a[::2]
even=a[1::2]
odd.sort()
even.sort()
a=[]
for i in range(len(even)):
    a.append(odd[i])
    a.append(even[i])

if len(odd)>len(even):
    a.append(odd[-1])
print(a)