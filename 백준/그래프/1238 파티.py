import sys
from queue import PriorityQueue
input = sys.stdin.readline

def dijkstra(start, dest):
  pq = PriorityQueue()
  pq.put((0, start))   # (거리, 번호)
  dist = [sys.maxsize for _ in range(n)]
  dist[start] = 0

  while pq:
    cur_dist, cur = pq.get()
    if cur == dest:
      return cur_dist
    
    for move, time in town[cur]:
      if cur_dist + time < dist[move]:
        dist[move] = cur_dist + time
        pq.put((dist[move], move))

n, m, x = map(int, input().split())   # n: 마을 개수, m: 도로 개수, x: 파티하는 마을
town = [[] for _ in range(n)]
for _ in range(m):
  v1, v2 , t = map(int, input().split())   # v1: 시작점, v2: 끝점, t: 도로를 지나는데 필요한 소요시간
  town[v1-1].append((v2-1, t))

max_time = 0
for i in range(n):
  if i == x-1:
    continue
  max_time = max(max_time, dijkstra(i, x-1) + dijkstra(x-1, i))

print(max_time)
