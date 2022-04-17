N = int(input())
pinary = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        pinary[i] = (0, 1)
    elif i == 1:
        pinary[i] = (1, 0)  # (0으로 끝나는 문자열 개수, 1로 끝나는 문자열 개수)
    else:
        pinary[i] = (pinary[i-1][0] + pinary[i-1][1], pinary[i-1][0])

print(pinary[-1][0] + pinary[-1][1])
