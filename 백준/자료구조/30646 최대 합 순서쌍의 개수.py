import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dict = {}
nums_sum = [0] * n
nums_sum[0] = nums[0]

for i in range(n):
  if nums[i] in dict:
    dict[nums[i]].append(i)
  else:
    dict[nums[i]] = [i]
  
for i in range(1, n):
  nums_sum[i] = nums_sum[i-1] + nums[i]

max_sum = 0
max_cnt = 0
for key in dict.keys():
  s = dict[key][0] - 1
  e = dict[key][-1]
  if s < 0:
    part_sum = nums_sum[e]
  else:
    part_sum = nums_sum[e] - nums_sum[s]
  if max_sum < part_sum:
    max_sum = part_sum
    max_cnt = 1
  elif max_sum == part_sum:
    max_cnt += 1

print(max_sum, max_cnt)
