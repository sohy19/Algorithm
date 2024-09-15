import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

now_w = 0
now_h = 0
res = 0

for i in range(w):
  if now_h <= blocks[i]:
    for j in range(now_w+1, i):
      res += (now_h - blocks[j])
    now_w = i
    now_h = blocks[i]

if now_w != w-1:
  now_w = 0
  now_h = 0
  for i in range(w-1, -1, -1):
    if now_h < blocks[i]:
      for j in range(i+1, now_w):
        res += (now_h - blocks[j])
      now_w = i
      now_h = blocks[i]
 
print(res)
