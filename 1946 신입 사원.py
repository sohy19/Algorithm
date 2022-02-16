import sys
input = sys.stdin.readline

def recruiting(i):
    score[i].sort()
    cnt, interview_rank = score[i][0]   # 1번은 무조건 뽑음 (서류 등수 1등)
    for j in range(1, n[i]):
        if score[i][j][1] < interview_rank:
            interview_rank = score[i][j][1]
            cnt += 1
    return cnt

t = int(input())
n = []
score = []
for i in range(t):
    n.append(int(input()))
    score.append([list(map(int, input().split())) for _ in range(n[i])])   # [서류 등수, 면접 등수]

for i in range(t):
    print(recruiting(i))