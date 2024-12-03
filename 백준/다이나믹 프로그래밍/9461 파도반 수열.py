import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    fn = [0] * (n+1)

    for i in range(1, n+1):
        if i == 1 or i == 2 or i == 3:
            fn[i] = 1
        else:
            fn[i] = fn[i-3] + fn[i-2]

    print(fn[n])
