import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

num = sum(visit[:x])
max_num = num
max_cnt = 1

for i in range(n-x):
  num = num - visit[i] + visit[i+x]

  if max_num < num:
    max_num = num
    max_cnt = 1

  elif max_num == num:
        max_cnt += 1

if max_num == 0:
  print("SAD")
else:
  print(max_num)
  print(max_cnt)
