import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 깊이 우선 탐색
def dfs3(adjList, v, visited):
    visited[v] = True
    for i in range(len(adjList[v])):
        w = adjList[v][i]
        if visited[w] == False:
            dfs3(adjList, w, visited)

# 그래프 생성
n, m = map(int, input().split())
adjList = [[] for _ in range(n)]   # list of lists 인접 리스트 그래프
for i in range(m):
    v1, v2 = map(int, input().split())
    adjList[v1-1].append(v2-1)
    adjList[v2-1].append(v1-1)

# 그래프 탐색
visited = [False for _ in range(n)]   # 방문 여부 확인 list
cnt = 0   # connected component 개수
for i in range(n):
    if visited[i] == False:
        dfs3(adjList, i, visited)
        cnt += 1

print(cnt)