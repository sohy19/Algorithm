import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False for _ in range(100001)]
q = deque()
q.append((n, 0))
res = 0

while q:
  x, s = q.popleft()

  if x == k:
    res = s
    break

  nx = x * 2
  if 0 <= nx <= 100000 and not visited[nx]:
    q.append((nx, s))
    visited[nx] = True
  
  for dx in (-1, 1):
    nx = x + dx
    if 0 <= nx <= 100000 and not visited[nx]:
      q.append((nx, s+1))
      visited[nx] = True


print(res)
