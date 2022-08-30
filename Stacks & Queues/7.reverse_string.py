str="GeeksforGeeks"
stac=[]
for i in range(len(str)):
    stac.append(str[i])
str=""
while stac:
    str=str+stac.pop()
print(str)