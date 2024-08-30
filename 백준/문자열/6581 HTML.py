import sys
lines = sys.stdin.readlines()

length = 0
for line in lines:
  line_list = list(line.split())
  for char in line_list:
    if char == "<br>":
      print()
      length = 0
    elif char == "<hr>":
      if length != 0:
        print()
      print("--------------------------------------------------------------------------------")
      length = 0
    else:
      if length + len(char) + 1 > 80:
        print()
        length = 0
      if length > 0:
        print(end=' ')
      length += len(char) + 1
      print(char, end='')
