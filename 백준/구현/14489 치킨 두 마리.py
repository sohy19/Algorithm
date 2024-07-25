a, b = map(int, input().split())
price = int(input())

if price * 2 <= a + b:
  print(a + b - price * 2)
else:
  print(a + b)
