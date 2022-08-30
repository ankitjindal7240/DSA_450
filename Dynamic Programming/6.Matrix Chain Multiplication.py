import sys
arr=[30,40,50,30,20,10,60]
mn= sys.maxsize
matrix=[]
for i in range(len(arr)):
    matrix.append([0]*len(arr))
def solve(arr,i,j):
    #write dp code
    global mn
    if i>=j:
        return 0
    for k in range(i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j)+ arr[i]*arr[k]*arr[j]
        if temp<mn:
            mn=temp

    return temp

"""
Venue:
Shivam Marrige Garden
125, Savitri Vihar, Sanganer, Sector 9, 
Pratap Nagar, Jaipur, Rajasthan 302033
Mob: 9013001288, 9549577711
"""