a1=[1,2,3,4,5,8]
a2=[6]
union=[]
intersection=[]
j=0
i=0
while i < len(a1) and j < len(a2):
    if a1[i] == a2[j]:
        union.append(a1[i])
        intersection.append(a1[i])
        i=i+1
        j=j+1
    else:
        if a1[i]>a2[j]:
            union.append(a2[j])
            j=j+1
        else:
            union.append(a1[i])
            i=i+1
if i==len(a1):
    for i in range(j,len(a2)):
        union.append(a2[i])
else:
    for j in range(i,len(a1)):
        union.append(a1[j])
print(union,intersection)
