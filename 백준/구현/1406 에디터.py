import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())
m = int(input())

before = deque(string)   # 커서 기준 앞
after = deque()   # 커서 기준 뒤

for _ in range(m):
  order = tuple(input().split())
  
  if order[0] == "L":
    if before:
      after.appendleft(before.pop())
  elif order[0] == "D":
    if after:
      before.append(after.popleft())
  elif order[0] == "B":
    if before:
      before.pop()
  else:
    before.append(order[1])

print(*before, *after, sep="")
