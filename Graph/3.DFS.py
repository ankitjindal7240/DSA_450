def dfs(root,visited,graph):
    visited.add(root)
    print(root)
    for neighbour in graph[root]:
        if neighbour not in visited:
            dfs(neighbour,visited,graph)

# visited =set()
# 2 using stack
def dfs2(root,graph,):
    visited = set()
    stack=[]
    stack.append(root)

    while stack:
        node=stack.pop()
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
