# nCr modulo 10^9 + 7
def nCr(n,r):
    matrix=[]
    for i in range(n+1):
        matrix.append([0]*(r+1))
        if r==n:
            return 1
        elif r>n:
            return 0
    def fact(n,r):
        if n==0 or r==0:
            if r!=0:
                return 0
            return 1
        if matrix[n][r]:
            return matrix[n][r]

        matrix[n][r]= (fact(n-1,r-1) + fact(n-1,r))%1000000007
        return matrix[n][r]
    return fact(n,r)

print(nCr(10000,30))