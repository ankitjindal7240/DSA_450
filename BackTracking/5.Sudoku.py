def isSafe(grid,row,col,item):
    for i in range(9):
        if grid[i][col]==item:
            return

    for i in range(9):
        if grid[row][i]==item:
            return

    for i in range(3):
        for j in range(3):
            r=3*(row//3)
            c=3*(col//3)
            if grid[i+r][j+c]==item:
                return
    return True

def sodukuSolver(grid,n,row,col):
    if col==n and row == n-1:
        return True
    if col == n :
        row=row+1
        col=0
    if grid[row][col]==0:

        for i in range(1,10):
            if isSafe(grid,row,col,i):
                grid[row][col] = i
                if sodukuSolver(grid,n,row,col+1):
                    return True
                grid[row][col] = 0
        return False

    else:
        if sodukuSolver(grid, n, row, col + 1):
            return True




grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

sodukuSolver(grid,len(grid),0,0)

for row in grid:
    print(row)