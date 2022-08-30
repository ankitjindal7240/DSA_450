def bfs(root,graph):
    visited=[0]*len(graph)
    visited[0]=1
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        print(node)

        for neighbour in graph[node]:
            if visited[neighbour]!=1:
                queue.append(neighbour)
                visited[neighbour] = 1