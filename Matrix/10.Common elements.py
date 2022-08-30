mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
row_len=len(mat[0])
col_len=len(mat)
dict={}
for i in range(row_len):
    dict[mat[0][i]]=1

for i in range(1,col_len):
    for j in range(row_len):
        if (mat[i][j] in dict) and dict[mat[i][j]]==i:
            dict[mat[i][j]] += 1

            if i==col_len-1:
                print(mat[i][j],end=" ")
