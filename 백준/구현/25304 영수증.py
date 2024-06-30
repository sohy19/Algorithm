total_price = int(input())
n = int(input())
res = 0

for _ in range(n):
    price, num = map(int, input().split())
    res += price * num

if total_price == res:
    print("Yes")
else:
    print("No")
