import sys
imput = sys.stdin.readline

need_player = {
  "Y": 1,
  "F": 2,
  "O": 3
}

N, game_type = input().split()
player = set()

for _ in range(int(N)):
  player.add(input())

print(len(player) // need_player[game_type])
