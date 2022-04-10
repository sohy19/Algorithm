N, K = map(int, input().split())    # 물품의 수, 무게
w = [0]  # 무게
v = [0]  # 가치
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

f = [[0 for j in range(K+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if i == 1:
            if w[i] > j:
                continue
            else:
                f[i][j] = v[i]
        else:
            if w[i] > j:
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = max(v[i]+f[i-1][j-w[i]], f[i-1][j])
print(f[i][j])
