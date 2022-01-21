def catalan(n):
    if (n == 0 or n == 1):
        return 1
    catalan_no=[0]*(n+1)
    catalan_no[0]=1
    catalan_no[1]=1
    for i in range(2,n+1):
        for j in range(i):
            catalan_no+=catalan_no[j]*catalan_no[i-j-1]
    return catalan_no[n]