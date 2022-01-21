from _collections import defaultdict
str="geeksforgeeks"
count=defaultdict(int)
for i in range(len(str)):
    count[str[i]] +=1

print(count)