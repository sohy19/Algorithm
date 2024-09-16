import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
stack = []
stack.append((height[n-1], n-1))
res = [0] * n

for i in range(n-2, -1, -1):
  while stack and height[i] > stack[-1][0]:
    res[stack.pop()[1]] = i+1
  stack.append((height[i], i))

print(*res)
