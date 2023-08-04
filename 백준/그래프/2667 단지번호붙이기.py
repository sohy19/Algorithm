import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(g, visited, i, j, n, cnt):
    visited[i][j] = True
    cnt += 1
    if j < n-1:   # 오른쪽 이동
        if g[i][j+1] == '1' and visited[i][j+1] == False:
            cnt = dfs(g, visited, i, j+1, n, cnt)
    if j > 0:   # 왼쪽 이동
        if g[i][j-1] == '1' and visited[i][j-1] == False:
            cnt = dfs(g, visited, i, j-1, n, cnt)
    if i < n-1:   # 아래쪽 이동
        if g[i+1][j] == '1' and visited[i+1][j] == False:
            cnt = dfs(g, visited, i+1, j, n, cnt)
    if i > 0:   # 위쪽 이동
        if g[i-1][j] == '1' and visited[i-1][j] == False:
            cnt = dfs(g, visited, i-1, j, n, cnt)
    return cnt

n = int(input())   # 지도 크기
map_ = []   # 단지 지도
section = 0   # 단지 수
house_num = []   # 단지내 집 수
for _ in range(n):
    map_.append(input())

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if map_[i][j] == '1' and visited[i][j] == False:
            cnt = dfs(map_, visited, i, j, n, 0)
            house_num.append(cnt)
            section += 1

house_num.sort()
print(section)
for i in range(len(house_num)):
    print(house_num[i])