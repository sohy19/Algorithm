import sys
input = sys.stdin.readline

t = int(input())   #  테스트 케이스 개수
for _ in range(t):
  n, m = map(int, input().split())   # n: 국가 수, m: 비행기 종류
  g = [[] for _ in range(n)]
  visited = [True for _ in range(n)]
  for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1-1].append(v2-1)
  print(n-1)
