# 마지막날부터 제일 맛있는 거 선택
import sys

n, t = map(int, input().split())    # 당근 종류, 일수
sweet = []
for i in range(n):
    w, p = map(int, sys.stdin.readline().split())   # 기본 맛, 영양제 
    sweet.append([p, w])     # 영양제, 기본 맛 순서로 리스트 저장 (리스트 형태로)

sweet.sort()	# 영양제를 기준으로 오름차순 정렬
max_eat = 0

for i in range(n):
    eat = sweet.pop()
    max_eat += eat[1] + (eat[0] * (t-(1+i)))
    
print(max_eat)
