from collections import defaultdict

graph=defaultdict(list)
v=6
indegree=[0]*v
visited=[0]*v
# directional
def addEdge(graph,source,dest):
    graph[source].append(dest)
    indegree[dest]+=1

addEdge(graph,5,2)
addEdge(graph,5,0)
addEdge(graph,4,0)
addEdge(graph,4,1)
addEdge(graph,2,3)
addEdge(graph,3,1)
print(indegree)
print(graph)
print(len(graph))
def topological(indegre,visited):
    for i in range(len(indegree)):
        if indegree[i]==0 and visited[i]==0:
            visited[i]=1
            print(i)
            for neighbours in graph[i]:
                indegree[neighbours]-=1
    for j in visited:
        if j==0:
            topological(indegre,visited)
def topologicalDFSUTil(node,visited,stack):
    visited[node]=1
    for neighbour in graph[node]:
        if visited[neighbour] == 0:
            topologicalDFSUTil(neighbour,visited,stack)
    stack.append(node)

def topologicalDFS(graph):
    visited = [0] * (len(graph)+1)
    stack=[]
    for node in graph:
        if visited[node] == 0:
            topologicalDFSUTil(node,visited,stack)

    print(stack[::-1])


topologicalDFS(graph)






# topological(indegree,visited)





