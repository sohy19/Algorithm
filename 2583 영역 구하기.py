import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(g, i, j, m, n, area):
    area += 1
    g[i][j] = (1, True)
    if j < n-1:   # 오른쪽 이동
        if g[i][j+1] == (1, False):
            area = dfs(g, i, j+1, m, n, area)
    if j > 0:   # 왼쪽 이동
        if g[i][j-1] == (1, False):
            area = dfs(g, i, j-1, m, n, area)
    if i < m-1:   # 위쪽 이동
        if g[i+1][j] == (1, False):
            area = dfs(g, i+1, j, m, n, area)
    if i > 0:   # 아래쪽 이동
        if g[i-1][j] == (1, False):
            area = dfs(g, i-1, j, m, n, area)
    return area      

m, n, k = map(int, input().split())   # 세로, 가로, 직사각형 개수
grid = [[(1, False) for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = (0, False)

cnt = 0   # 영역 개수
area = []   # 각 영역 넓이
for i in range(m):
    for j in range(n):
        if grid[i][j] == (1, False):
            ar = dfs(grid, i, j, m, n, 0)
            area.append(ar)
            cnt += 1

print(cnt)
area.sort()
for i in range(len(area)):
    print(area[i], end=' ')