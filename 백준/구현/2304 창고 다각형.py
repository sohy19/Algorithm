import sys
input = sys.stdin.readline

n = int(input())
stick = []

for _ in range(n):
  stick.append(tuple(map(int, input().split())))

stick.sort(key = lambda x: (x[0]))

res = 0
width = height = 0
last_idx = 0

for i in range(n):
  if height <= stick[i][1]:
    res += (stick[i][0] - width) * height
    width = stick[i][0]
    height = stick[i][1]
    last_idx = i

width = height = 0
for i in range(n-1, last_idx-1, -1):
  if height <= stick[i][1]:
    res += (width - stick[i][0]) * height
    width = stick[i][0]
    height = stick[i][1]

print(res + height)
