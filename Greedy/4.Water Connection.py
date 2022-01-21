
def solve( n, p, a, b, d):
    incoming, outgoing = [0] * (n + 1), [0] * (n + 1)
    graph = [None] * (n + 1)
    visited = [0] * (n + 1)
    ans = []

    for i in range(p):
        incoming[b[i]] = 1
        outgoing[a[i]] = 1
        graph[a[i]] = (b[i], d[i])

    def dfs(graph, start, min_dia):
        visited[start] = 1
        if graph[start] is None:
            return start, min_dia
        return dfs(graph, graph[start][0], min(graph[start][1], min_dia))

    for i in range(1, n + 1):
        if not visited[i] and not incoming[i] and outgoing[i]:
            end, mid_dia = dfs(graph, i, graph[i][1])
            ans.append((i, end, mid_dia))

    return ans
n = 9
p = 6
a =[7,5,4,2,9,3]
b =[4,9,6,8,7,1]
d =[98,72,10,22,17,66]
print(solve(n, p, a, b, d))

