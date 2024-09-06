import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v, d):
  global t
  visited[v] = True
  depth[v] = d
  order[v] = t
  t += 1

  for w in graph[v]:
    if not visited[w]:
      dfs(w, d+1)


n, m, r = map(int, input().split())   # n: 정점 수, m: 간선 수, r: 시작 정점
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
depth = [-1 for _ in range(n)]
order = [0 for _ in range(n)]

for _ in range(m):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  graph[v-1].append(u-1)

for i in range(n):
  graph[i].sort(reverse=True)

t = 1
dfs(r-1, 0)   # dfs(정점, 깊이, 방문 순서)
print(sum(list(depth[i] * order[i] for i in range(n))))
