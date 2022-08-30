def mah(arr):
    pass
def max_rectangle(mat):
    n=len(mat)
    arr=mat[0]
    mx_area=mah(arr)
    for i in range(1,n):
        for j in range(n):
            if mat[i][j]==0:
                pass
            else:
                mat[i][j]=mat[i][j]+mat[i-1][j]
        area=mah(arr)
        if area>mx_area:
            mx_area=area
    return mx_area

"""
mah is maximim area of histogram , for each row if column is 0 then left unchanged else add prev row element
"""