import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
res = [0] * n

for i in range(n):
  idx = 0
  goal = nums[i]

  while idx <= goal:
    if res[idx] != 0:
      goal += 1
    idx += 1
  
  res[goal] = i + 1

print(*res)
