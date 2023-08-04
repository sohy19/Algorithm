n = int(input())
enjoy = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        continue
    else:
        for j in range(1, i//2+1):
            enjoy[i] = max(enjoy[i], j * (i-j) + enjoy[j] + enjoy[i-j])

print(enjoy[-1])
