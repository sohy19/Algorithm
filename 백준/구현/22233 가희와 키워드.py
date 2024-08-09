import sys

input = sys.stdin.readline

n, m = map(int, input().split())
keywords = {}
nums = n
for _ in range(n):
  keywords[input().strip()] = 1

for _ in range(m):
  memo = list(input().strip().split(","))

  for name in memo:
    if name in keywords and keywords[name] == 1:
      keywords[name] = 0
      nums -= 1

  print(nums)
