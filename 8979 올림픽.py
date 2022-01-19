import sys
input = sys.stdin.readline

N, k = map(int, input().split())    # 국가 수, 등수를 알고 싶은 국가 번호
nation = []   # 국가 번호와 매달 정보 저장

for i in range(N):
    nation.append(list(map(int, input().split())))   # [국가 번호, 금, 은, 동]

rank = sorted(nation, key = lambda x : (-x[1], -x[2], -x[3]))   # 금 > 은 > 동 우선 순위로 정렬된 nation 리스트

same = 0   # 같은 등수
now_rank = 1   # 현재 등수

for i in range(1, N):
    if rank[0][0] == k:   # 등수를 알고 싶은 국가가 1등일 경우
        break
    if rank[i][1] == rank[i-1][1] and rank[i][2] == rank[i-1][2] and rank[i][3] == rank[i-1][3]:   # 이전 국가와 매달이 같을 경우
        same += 1
    else:
        now_rank = now_rank + 1 + same
        same = 0
    if rank[i][0] == k:
        break

print(now_rank)