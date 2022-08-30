import sys
arr = [7, 4, 8, 8, 8, 9]
k=6
ans=sys.maxsize
arr.sort()
print(arr)
ans= arr[-1] - arr[0]   # max possible diff
# print(ans)
for i in range(1,len(arr)):
    tempmin=min(arr[0]+k,arr[i]-k)                      #decementing every no
    tempmax=max(arr[-1]-k,arr[i-1]+k)                   # incrementing every previous(smaller) no

    ans=min(ans,tempmax-tempmin)                        # checking diff between adjacent two no because only it can be min

print(ans)