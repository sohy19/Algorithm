import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())   # 점수 개수, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수 개수
if n == 0:   # 리스트에 점수가 하나도 없을 경우
    print(1)
    exit()
scores = list(map(int, input().split()))   # 랭킹 리스트

high_score = 0   # 태수 점수보다 높은 점수의 개수
same_score = 0   # 태수 점수와 같은 점수의 개수
for i in range(n):
    if scores[i] > new_score:
        high_score += 1
    elif scores[i] == new_score:
        same_score += 1

if high_score + same_score >= p:
    print(-1)
else:
    print(high_score+1)
    