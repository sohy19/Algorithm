import sys
input = sys.stdin.readline

n = int(input())
fn = [0] * (n + 1)

for i in range(n+1):
    if i == 0:
        fn[i] = 0
    elif i == 1:
        fn[i] = 1
    else:
        fn[i] = fn[i-1] + fn[i-2]

print(fn[n])
