import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int, input().split()))

height = lights[0]
height = max(N - lights[M-1], height)

for i in range(M-1):
  height = max((lights[i+1] - lights[i] + 1) // 2, height)

print(height)
