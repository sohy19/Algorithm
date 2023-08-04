import sys

N = int(sys.stdin.readline())   # 채널 수
channel = []   # 채널 이름 리스트
for i in range(N):
    channel.append(input())


kbs1 = channel.index("KBS1")
kbs2 = channel.index("KBS2")

if kbs1 == 0 and kbs2 == 1:
    final_move = ''
else:
    move1 = "1" * kbs1 + "4" * kbs1

    if kbs2 < kbs1 :   # KBS1이 KBS2 채널보다 앞에 있을 때
        move2 = "1" * kbs2 + "4" * kbs2
        final_move = move1 + "1" + move2
    else:   # KBS2가 KBS1 채널보다 앞에 있을 때
        move2 = "1" * kbs2 + "4" * (kbs2-1)
        final_move = move1 + move2

print(final_move)