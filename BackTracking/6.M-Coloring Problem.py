# # backtrecking
# colours=5
from _collections import defaultdict

graph=defaultdict(list)

def addEdgeND(graph,source,dest):
    graph[source].append([dest,0])
    graph[dest].append([source,0])

def issafe(graph,node,color):
    for neighbour in graph[node][0]:
        if graph[node][1]==color:
            return False
    return True
def colour_graph(graph,node,colors):
    if node>=len(graph):
        return True
    for color in range(1,colors+1):
        if issafe(graph,node,color):
            graph[node][1]=color
            if colour_graph(graph,node+1,colors):
                return True
            graph[node][1] = 0
    return False

# # DFS

graph2=defaultdict(list)
nodes=[]
for i in range(len(graph2)):
    nodes.append(i)
def addEdgeND2(graph2,source,dest):
    graph2[source].append([dest,1])
    graph2[dest].append([source,1])
def colourgraph2(graph,max_colours):
    used_colours=1
    visited=set()
    q=[]
    for i in range(len(nodes)):
        if i not in visited:
            visited.add(i)
            q.append(i)
        while q:
            node=q.pop(0)
            for neighbour in graph2[node]:
                if neighbour[1]==node[1]:
                    neighbour[1]=neighbour[1]+1
                    used_colours=max(max_colours,neighbour[1],node[1])
                    if used_colours>max_colours:
                        return False
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
    return True
n=5
qu=[]
qu.append(n)
n=n+1
print(qu)