import collections

def dfs(visited,order,graph,nodes,u):
    visited[u] = True
    loc = graph[u]
    for item in loc:
        if visited[item] == False:
            dfs(visited,order,graph,nodes,item)

    order.append(u)

temp = ["cca","aaa","aab"]
nodes = set()
for i in range(len(temp)):
    for j in range(len(temp[i])):
        nodes.add(temp[i][j])

graph = collections.defaultdict(set)

for i in range(len(temp)-1):
    for j in range(min(len(temp[i]),len(temp[i+1]))):
        if(temp[i][j]!=temp[i+1][j]):
            graph[temp[i][j]].add(temp[i+1][j])


visited = collections.defaultdict()
for item in nodes:
    visited[item] = False
order= []
for item in nodes:
    if(visited[item] == False):
        dfs(visited,order,graph,nodes,item)

print(order[::-1])