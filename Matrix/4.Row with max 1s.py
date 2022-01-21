def maxOnes(matrix,n,m):
    row=0
    col=m-1
    ans=-1
    while row<n and col>=0:
        if matrix[row][col]==1:
            ans=row
            col=col-1
        else: row=row+1
    return ans
