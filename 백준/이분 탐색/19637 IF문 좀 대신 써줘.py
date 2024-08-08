import sys

input = sys.stdin.readline

n, m = map(int, input().split())    # n: 칭호 개수, m: 캐릭터 개수
nickname = {}
level = []

def findNickname(power):
  start = 0
  end = len(level) - 1

  while start <= end:
    mid = (start + end) // 2
    if power <= int(level[mid]):
      end = mid - 1
    else:
      start = mid + 1
  
  return nickname[level[start]]

for _ in range(n):
  val = tuple(input().split())
  if not val[1] in nickname:
    nickname[val[1]] = val[0]
    level.append(val[1])

for _ in range(m):
  print(findNickname(int(input())))
