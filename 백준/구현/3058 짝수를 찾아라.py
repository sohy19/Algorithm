import sys

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    even_sum = 0
    even_min = sys.maxsize
    for num in nums:
        if num % 2 == 0:
            even_sum += num
            even_min = min(even_min, num)
    print(even_sum, even_min)
