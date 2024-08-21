import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
  return 0 <= x < n and 0 <= y < m

def bfs():
  q = deque()
  q.append((dest[0], dest[1]))

  while q:
    x, y = q.popleft()
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
      nx = x + dx
      ny = y + dy
      if in_range(nx, ny) and grid[nx][ny] != 0 and grid[nx][ny] != 2 and dist[nx][ny] == 0:
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

for i in range(n):
  grid.append(list(map(int, input().split())) for _ in range(n))
  if 2 in grid[i]:
    for j in range(m):
      if grid[i][j] == 2:
        dest = (i, j)
        break


bfs()
for i in range(n):
  for j in range(m):
    if grid[i][j] != 0 and grid[i][j] != 2 and dist[i][j] == 0:
      print(-1, end=' ')
    else:
      print(dist[i][j], end=' ')
  print()
