while True:
  try:
    n = int(input())
    for i in range(int(n)+1):
      if i == 0:
        str = "-"
      else:
        str = str + " " * len(str) + str
    print(str)
  except EOFError:
    break
