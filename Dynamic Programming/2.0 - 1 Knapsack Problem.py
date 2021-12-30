N = 3
W = 4
values = [1,2,3]
weight = [4,5,1]
matrix=[]
for i in range(N+1):
    matrix.append([0]*(W+1))
for n in range(1,N+1):
    for w in range(1,W+1):
        if weight[n-1]<=w:
            matrix[n][w]=  max((values[n-1] + matrix[n-1][w - values[n-1]] ), matrix[n-1][w])
        else:
            matrix[n][w] =  matrix[n - 1][w]

print(matrix)