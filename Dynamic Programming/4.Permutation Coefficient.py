def permutation(n,r):
    matrix=[]
    for i in range(n+1):
        matrix.append([0]*(r+1))
        if r==n:
            return 1
        elif r>n:
            return 0

    def nPr(n,r):
        if n==0 or r==0:
            if r!=0:
                matrix[n][r]=0
                return  0
            matrix[n][r]=1
            return 1
        if matrix[n][r]:
            return matrix[n][r]
        matrix[n][r] = nPr(n-1,r) + r*nPr(n-1,r-1)
        return matrix[n][r]
    nPr(n,r)
    print(matrix)
    return matrix[-1][-1]

def permutation2(n,r):
    ans=1
    for i in range(1,r+1):
        ans=ans*(n-r+i)

    return ans
print(permutation2(10,0))
print(permutation(10,2))

