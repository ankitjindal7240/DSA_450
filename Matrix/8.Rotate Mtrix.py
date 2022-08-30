m = [[1, 2,  3,  4],
     [5, 6,  7,  8],
     [9, 10, 11, 12],
     [13,14, 15, 16]]


def rotate(m):
     #transopse by swapinfg row and col elements
     n=len(m)
     for i in range(n):
          for j in range(i,n):     # if all elements  treversed it will again transpose matrix
               m[i][j],m[j][i]=m[j][i],m[i][j]

     #revese rows
     for i in range(n):
          m[i]=m[i][::-1]
     for item in m :
          print(item)


rotate(m)