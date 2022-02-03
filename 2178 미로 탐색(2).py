import sys, copy
input = sys.stdin.readline

def maze_exploration(g, m, n, visited):
    queue = [(0, 0)]
    visited[0][0] = 1
    while queue:
        if visited[n-1][m-1] != 0:
            return visited[n-1][m-1]
        i, j = queue.pop(0)
        if j < m-1:   # 오른쪽 이동
            if g[i][j+1] == '1' and visited[i][j+1] == 0:
                visited[i][j+1] = visited[i][j] + 1
                queue.append((i, j+1))
        if j > 0:   # 왼쪽 이동
            if g[i][j-1] == '1' and visited[i][j-1] == 0:
                visited[i][j-1] = visited[i][j] + 1
                queue.append((i, j-1))
        if i < n-1:   # 아래쪽 이동
            if g[i+1][j] == '1' and visited[i+1][j] == 0:
                visited[i+1][j] = visited[i][j] + 1
                queue.append((i+1, j))
        if i > 0:   # 위쪽 이동
            if g[i-1][j] == '1' and visited[i-1][j] == 0:
                visited[i-1][j] = visited[i][j] + 1
                queue.append((i-1, j))

n, m = map(int, input().split())   # 행, 열
maze = []   # 미로
for _ in range(n):
    maze.append(input())
visited = [[0 for _ in range(m)] for _ in range(n)]
min_cnt = maze_exploration(maze, m, n, visited)
print(min_cnt)