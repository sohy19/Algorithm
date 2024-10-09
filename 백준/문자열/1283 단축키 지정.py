import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
  string = list(input().split())
  length = len(s)

  for i in range(len(string)):
    s.add(string[i][0].upper())
    if length < len(s):
      string[i] = "[" + string[i][0] + "]" + string[i][1:] 
      break
  else:
    for i in range(len(string)):
      for j in range(len(string[i])):
        s.add(string[i][j].upper())
        if length < len(s):
          string[i] = string[i][:j] + "[" + string[i][j] + "]" + string[i][j+1:]
          break
      if length < len(s):
        break
  print(*string)
