import sys
input = sys.stdin.readline

n = int(input())
fn = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        fn[i] = 1
    elif i == 2:
        fn[i] = 3
    else:
        fn[i] = fn[i-1] + fn[i-2] * 2

print(fn[n] % 10007)
