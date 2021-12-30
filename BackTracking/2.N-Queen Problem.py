n=5

matrix=[]
for i in range(n):
    matrix.append([0]*n)
def isSafe(row,col,n):
    for ro in range(row):
        if matrix[ro][col]==1:
            return False
    i=row
    j=col
    while i>=0 and j>=0:
        if matrix[i][j]==1:
            return False
        i=i-1
        j=j-1

    i=row
    j=col
    while i>=0 and j<n-1:
        if matrix[i][j]==1:
            return False
        i=i-1
        j=j+1
    return True

def nQueen(matrix,row,n):
    if row>=n:
        for m in matrix:
            print(m)
        print(" ")
        return 1
    for col in range(n):
        if isSafe(row,col,n):
            matrix[row][col]=1

            if nQueen(matrix,row+1,n):
                return 1                #if we want to print all solutins don't return
            matrix[row][col] = 0
    return
nQueen(matrix,0,5)