n = int(input())
grid = [list(input()) for _ in range(n)]

result = []
size = n
def calc(i, j, size):
  if same(i, j, size):
    result.append(grid[i][j])
    return
  else:
    size //= 2
    result.append("(")
    calc(i, j, size)  # 제1사분면
    calc(i, j + size, size)  # 제2사분면
    calc(i + size, j, size)  # 제3사분면
    calc(i + size, j + size, size)  # 제4사분면
    result.append(")")
  
def same(i, j, size):
  ch = grid[i][j]
  for x in range(size):
    for y in range(size):
      dx, dy = i + x, j + y
      if ch != grid[dx][dy]:
        return False
  return True


calc(0, 0, n)
for i in range(len(result)):
  print(result[i], end="")
