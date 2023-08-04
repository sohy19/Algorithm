n = int(input())
C = [0 for i in range(n+1)]  # 방법의 수

for i in range(1, n+1):
    if i == 1:
        C[i] = 1
    elif i == 2:
        C[i] = 2
    else:
        C[i] = C[i-1] + C[i-2]

print(C[n]%10007)
