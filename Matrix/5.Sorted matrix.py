mat=[[10,20,30,40],
[15,25,35,45],
[27,29,37,48],
[32,33,39,50]]
n=len(mat)

ans=[]
for i in range(n):
    for j in range(n):
        ans.append(mat[i][j])
ans.sort()
j=0
mat=[]

for i in range(n):
    mat.append(ans[j:j+n])
    j=j+n
print(mat)