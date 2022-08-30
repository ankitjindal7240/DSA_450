import sys
mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1,   3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]
n=len(mat)
maxv=mat[-1][-1] #initialise

# preprocess last row
for i in reversed(range(n)):
    if mat[-1][i]>maxv:
        maxv =mat[-1][i]
    mat[-1][i]=maxv

# preproccee last col
maxv=mat[-1][-1] #initialise
for j in reversed(range(n)):
    if mat[j][-1]>maxv:
        maxv=mat[j][-1]
    mat[j][-1]=maxv

maxValue = -sys.maxsize -1  #initialise

#  from bottom elements
for i in reversed(range(n-1)):
    for j in reversed(range(n-1)):
        maxValue=max(mat[+1][j+1]-mat[i][j] , maxValue)  # upadte max

        mat[i][j]=max(mat[i][j],
                      max(mat[i+1][j],mat[i][j+1]))  # update mat[i][j] for future

print(maxValue)

# O(n2)