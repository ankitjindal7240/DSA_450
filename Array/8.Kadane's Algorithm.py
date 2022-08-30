arr=[1,2,3,-2,5]
import sys
max_sum= -sys.maxsize
# print(max_sum)
s=0
for i in range(len(arr)):
    s=s+arr[i]
    if s>max_sum:
        max_sum=s
    if s<0:
        s=0
print(max_sum)