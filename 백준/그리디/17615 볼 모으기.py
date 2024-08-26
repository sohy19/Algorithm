import sys
input = sys.stdin.readline

n = int(input())
color = input().strip()
min_cnt = sys.maxsize

red_cnt = 0
blue_cnt = 0

for c in color:
  if c == "R":
    red_cnt += 1
  else:
    blue_cnt += 1

left_red_cnt = 0
right_red_cnt = 0
left_blue_cnt = 0
right_blue_cnt = 0

for i in range(n-1):
  if color[0] == "R":
    if color[i] == color[i+1]:
      left_red_cnt += 1
    else:
      left_red_cnt += 1
      break
  else:
    if color[i] == color[i+1]:
      left_blue_cnt += 1
    else:
      left_blue_cnt += 1
      break

for i in range(n-1, 0, -1):
  if color[n-1] == "R":
    if color[i] == color[i-1]:
      right_red_cnt += 1
    else:
      right_red_cnt += 1
      break
  else:
    if color[i] == color[i-1]:
      right_blue_cnt += 1
    else:
      right_blue_cnt += 1
      break

print(min(red_cnt - left_red_cnt, 
          red_cnt - right_red_cnt,
          blue_cnt - left_blue_cnt,
          blue_cnt - right_blue_cnt))


# ---------------------------------------------------------------


cnt = []
strip_color = color.lstrip("R")
cnt.append(strip_color.count("R"))
strip_color = color.rstrip("R")
cnt.append(strip_color.count("R"))
strip_color = color.lstrip("B")
cnt.append(strip_color.count("B"))
strip_color = color.rstrip("B")
cnt.append(strip_color.count("B"))
print(min(cnt))
