import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
put = [False for _ in range(n)]
q = deque()

for i in range(n-2, -1, -1):  # 스택 개수 = 큰 사람 수
  if nums[i] > len(q):
    j = 1
    while nums[i] > len(q):
      if not put[i+j]:
        q.append(i+j+1)
        put[i+j] = True
      j += 1
  elif nums[i] < len(q):
    temp = []
    for j in range(1,  len(q) - nums[i] + 1):
      temp.append(q.pop())
    q.append(i+1)
    put[i] = True
    for j in range(len(temp)-1, -1, -1):
      q.append(temp[j])


while q:
  print(q.popleft(), end=" ")

for i in range(n):
  if not put[i]:
    print(i+1, end=" ")
