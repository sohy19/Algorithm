from math import ceil

h, w, n, m = map(int, input().split())   # h: 행, w: 열, n: 세로 거리두기, m: 가로 거리두기

rows = ceil(h / (n + 1))
cols = ceil(w / (m + 1))
print(rows * cols)

# ------------------------------------------------------------

import math

h, w, n, m = map(int, input().split())

width = math.ceil(w / (m + 1))
height = math.ceil(h / (n + 1))

print(width * height)
