def dfs(graph,node,visited,curr_cycle):
    if visited[node]==True :
        if curr_cycle[node]==True:
            return True
        return False
    visited[node]=True
    curr_cycle[node]=True
    for neighbour in graph[node]:
        if dfs(graph,neighbour,visited,curr_cycle):
            return True
    curr_cycle[node] = False
    return False

def detectCycleDFS(graph):
    visited=[False]*len(graph)
    curr_cycle=[False]*len(graph)
    for node  in graph:
        if  dfs(graph,node,visited,curr_cycle):
            return True
    return False


