nums = input()
n = '0'
i = 0

while i < len(nums):
  n = str(int(n) + 1)
  for j in range(len(n)):
    if nums[i] == n[j]:
      i += 1
      if i == len(nums):
        break

print(n)
