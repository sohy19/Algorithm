socks = {}

for _ in range(5):
  num = int(input())
  if num in socks:
    del socks[num]
  else:
    socks[num] = 1

for num in socks.keys():
  print(num)
