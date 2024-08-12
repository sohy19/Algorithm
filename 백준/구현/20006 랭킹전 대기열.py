import sys
input = sys.stdin.readline

p, m = map(int, input().split())  # p: 플레이어 수, m: 방 정원

room = []
room_level = {}  # 방 기준 레벨

for _ in range(p):
  level, nickname = input().split()
  level = int(level)

  for key in room_level.keys():
    if len(room[key]) < m and abs(room_level[key] - level) <= 10:
      room[key].append((level, nickname))
      break
  else:
    room_level[len(room)] = level
    room.append([(level, nickname)])

for i in range(len(room)):
  if len(room[i]) == m:
    print("Started!")
  else:
    print("Waiting!")
  room[i].sort(key = lambda x: x[1])
  for player in room[i]:
    print(player[0], player[1])
