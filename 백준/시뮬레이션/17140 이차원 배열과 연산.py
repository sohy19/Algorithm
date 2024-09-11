import sys
from collections import Counter
input = sys.stdin.readline


def operation_R():
  global nums
  new_nums = []
  max_len = 0
  for i in range(len(nums)):
    counter = Counter(nums[i])
    counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    line = []
    for key, count in counter:
      if key == 0:
        continue
      line.append(key)
      line.append(count)

    line = line[:100]
    max_len = max(max_len, len(line))
    new_nums.append(line)
  
  for i in range(len(new_nums)):
    if len(new_nums[i]) < max_len:
      new_nums[i] = new_nums[i] + [0] * (max_len - len(new_nums[i]))

  nums = new_nums


r, c, k = map(int, input().split())   # r: 행, c: 열, k: 목표 값
nums = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
  try:
    if nums[r-1][c-1] == k:
      print(i)
      break
  except:
    pass
  if len(nums) >= len(nums[0]):
    operation_R()
  else:
    nums = list(map(list, zip(*nums)))
    operation_R()
    nums = list(map(list, zip(*nums)))

else:
  print(-1)
