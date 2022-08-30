matrix =    [[1, 2, 3, 4,25],
             [5, 6, 7, 8,26],
             [9, 10,11,12,27],
             [13,14,15,16,28],
             [17,18,19,20,29],
            ]












rows=len(matrix)-1
coulms=len(matrix[0])-1
no_of_rounds= (min(rows+1,coulms+1))//2 +(min(rows+1,coulms+1))%2
# print(no_of_rounds)
round=0
while no_of_rounds>round:
    for i in range(round, coulms-round+1):
        print(matrix[round][i], end=" ")
    for j in range(round+1,rows-round+1):
        print(matrix[j][-round-1], end=" ")

    for k in reversed(range(round,coulms-round)):
        print(matrix[-round-1][k], end=" ")
    for z in reversed(range(round+1,rows-round)):
        print(matrix[z][round], end=" ")
    round = round + 1
# recursive approach

