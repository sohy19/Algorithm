import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt = {}   # 원소 개수
length = max_length = start = end = 0

while start <= end and end < n:
  if nums[end] in cnt:
    if cnt[nums[end]] < k:
      cnt[nums[end]] += 1
      end += 1
    else:
      cnt[nums[start]] -= 1
      start += 1
  else:
    cnt[nums[end]] = 1
    end += 1
  max_length = max(max_length, end - start)
    
print(max_length)
