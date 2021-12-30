from _collections import defaultdict

graph=defaultdict(list)
# directional
def addEdge(graph,source,dest):
    graph[source].append(dest)

#non directional
def addEdgeND(graph,source,dest):
    graph[source].append(dest)
    graph[dest].append(source)
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
print(graph)