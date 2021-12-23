coins=[1,2,3,4,5]
s=5
l=len(coins)
matrix=[]
for i in range(l+1):
    matrix.append([0]*(s+1))
for i in range(l+1):
    matrix[i][0]=1

def coin_change(coins,s,l):
    if l==0:
        return 0
    if s==0:
        return 1
    if coins[l-1]<=s:
        return coin_change(coins,s-coins[l-1],l) + coin_change(coins,s,l-1)
    else:
        return coin_change(coins,s,l-1)

print(coin_change(coins,s,l))

def coin_change_dp(matrix,coins,s,l):
    if l==0:
        return 0
    if s==0:
        return 1
    if matrix[l][s]:
        return matrix[l][s]
    if coins[l-1]<=s:
         matrix[l][s]= coin_change_dp(matrix,coins,s-coins[l-1],l) + coin_change_dp(matrix,coins,s,l-1)
         return matrix[l][s]
    else:
        matrix[l][s] = coin_change_dp(matrix,coins,s,l-1)
        return matrix[l][s]
coin_change_dp(matrix,coins,s,l)

def coin_change_dp_2(coins,s,l):
    matrix = []
    for i in range(l + 1):
        matrix.append([0] * (s + 1))
    for i in range(l + 1):
        matrix[i][0] = 1
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            if coins[i-1]<=j:
                matrix[i][j]=matrix[i][j-coins[i-1]] + matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i - 1][j]
    for i in matrix:
        print(i)
    return matrix[-1][-1]
print(coin_change_dp_2(coins,s,l))




for i in matrix:
    print(i)

start= [75250, 50074 ,43659, 8931, 11273 ,27545, 50879 ,77924]
end =  [112960, 114515, 81825 ,93424 ,54316 ,35533 ,73383 ,160252]