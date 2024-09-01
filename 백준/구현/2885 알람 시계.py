h, m = map(int, input().split())
# now_h = now_m = 0

if m < 45:
  now_m = 15 + m
  if h == 0:
    now_h = 23
  else:
    now_h = h - 1
else:
  now_m = m - 45
  now_h = h

print(now_h, now_m)
