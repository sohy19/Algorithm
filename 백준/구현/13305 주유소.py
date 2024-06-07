import sys
input = sys.stdin.readline

n = int(input())   # 도시 개수
length = list(map(int, input().split()))   # 도로 길이
price = list(map(int, input().split()))   # 주유 가격

min_price = price[0]
total_price = 0

for i in range(n-1):
  total_price += length[i] * min_price
  min_price = min(min_price, price[i+1])

print(total_price)
