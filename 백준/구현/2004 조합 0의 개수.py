def calc(n, x):
    cnt = 0
    while x <= n:
        n = n // x
        cnt += n
    return cnt

n, m = map(int, input().split())
print(min(calc(n, 2) - calc(n-m, 2) - calc(m, 2), calc(n, 5) - calc(n-m, 5) - calc(m, 5)))
