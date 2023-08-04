import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(g, v, visited, route):
    route.append(v)
    visited[v] = True
    for i in range(len(g[v])):
        w = g[v][i]
        if visited[w] == False:
            dfs(g, w, visited, route)
    return route

def bfs(g, v, visited, route):
    visited[v] = True
    queue = [v]
    while len(queue) != 0:
        u = queue.pop(0)
        route.append(u)
        for w in g[u]:
            if visited[w] == False:
                queue.append(w)
                visited[w] = True
    return route

n, m, v = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색 시작한 정점 번호
g = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

for i in range(n):
    g[i+1].sort()

visited = [False for _ in range(n+1)]
dfs_route = dfs(g, v, visited, [])
visited = [False for _ in range(n+1)]
bfs_route = bfs(g, v, visited, [])

for i in range(len(dfs_route)):
    print(dfs_route[i], end=' ')
print()
for i in range(len(bfs_route)):
    print(bfs_route[i], end=' ')