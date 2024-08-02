t = int(input())
for _ in range(t):
    car = int(input())
    n = int(input())
    for _ in range(n):
        cnt, price = map(int, input().split())
        car += cnt * price
    print(car)
