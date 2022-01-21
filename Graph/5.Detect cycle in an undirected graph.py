visited=set()
def iscycle(graph,visited,parent):
    visited.add(parent)
    for neighbour in graph[parent]:
        if neighbour not in visited:
            iscycle(graph,visited,neighbour)
        elif neighbour!=parent:
            return True

    return False
