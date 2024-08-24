import sys
input = sys.stdin.readline

n, d = map(int, input().split())   # n: 지름길 개수, d: 고속도로 길이
route = [sys.maxsize] * (d + 1)
shortcut = [[] for _ in range(d+1)]

for _ in range(n):
  start, end, dist = map(int, input().split())
  if start <= d and end <= d:
    shortcut[start].append((end, dist))

route[0] = 0
for i in range(d+1):
  if i > 0:
    route[i] = min(route[i], route[i-1] + 1)
  
  for end, dist in shortcut[i]:
    route[end] = min(route[end], route[i] + dist)

print(route[d])
