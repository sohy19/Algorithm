dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inRange(i, j):
    return 0 <= i < n and 0 <= j < n

def dfs(x, y, cnt):
    visited[x][y] = False
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if inRange(nx, ny) and grid[nx][ny] - grid[x][y] == 1:
            cnt = dfs(nx, ny, cnt+1)
    return cnt

T = int(input())
for t in range(1, T+1):
    n = int(input())
    maxCnt = 0
    maxNum = 0
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[True for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt = dfs(i, j, 1)
                num = grid[i][j]
                if maxCnt == cnt:
                    if num < maxNum:
                        maxNum = num
                elif maxCnt < cnt:
                    maxCnt = cnt
                    maxNum = num
    print(f"#{t} {maxNum} {maxCnt}")
