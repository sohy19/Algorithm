s = input()
nums = [0 for _ in range(26)]

for ch in s:
  nums[ord(ch) - 97] += 1

print(*nums)
