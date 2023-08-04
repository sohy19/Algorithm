N = int(input())    # 퇴사일
T = []  # 상담을 완료하는데 걸리는 기간
P = []  # 상담을 했을 때 받을 수 있는 금액
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

profit = [0 for i in range(N+1)]  # 최대 이익

for i in range(N-1, -1, -1):
    if i == N-1 and i+T[i] == N:    # 마지막 날 상담 기간이 1일이어서 상담이 가능한 경우
        profit[i] = P[i]
    elif i+T[i] <= N:  
        profit[i] = max(P[i]+profit[i+T[i]], profit[i+1])
    else:   # 상담 기간이 퇴사일을 넘어갈 경우 (i일 날 상담 못 함)
        profit[i] = profit[i+1]

print(profit[0])
