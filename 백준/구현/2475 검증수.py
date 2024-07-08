nums = list(map(int, input().split()))
res = 0

for num in nums:
    res += num * num

print(res % 10)
