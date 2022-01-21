matrix = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
r=3
c=3
min,max=matrix[0][0]
for i in range(len(matrix)):
    if matrix[i][0]<min:
        min=matrix[i][0]
    if matrix[i][-1]>max:
        max=matrix[i][-1 ]
desired=(r*c)//2 +1
while min<max:
    mid=min+(max-min)//2

