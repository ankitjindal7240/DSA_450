n = 4
m =     [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]]

v=[]
for i in range(n):
    v.append([0]*(n))
ans=[]

def ratMaze(m,n,row,col,path):
    if row==col==n-1:
        ans.append(path)
        return

    if 0 <= row <= n - 1 and 0 <= col <= n - 1    and    m[row][col] == 1   and    v[row][col] == 0:
        v[row][col] = 1
        up=ratMaze(m,n,row-1,col,path+"u")
        down=ratMaze(m,n,row+1,col,path+"d")
        left=ratMaze(m,n,row,col-1,path+"l")
        right=ratMaze(m,n,row,col+1,path+"r")
        v[row][col] = 0
    return


#
ratMaze(m,n,0,0,"")
print(ans)