import sys
input = sys.stdin.readline

n, l = map(int, input().split())   # n: 물이 새는 곳 개수, l: 테이프 길ㅇ
spot = list(map(int, input().split()))

cnt = 0   # 테이프 개수
start = 0   # 테이프 시작 위치

while True:
    for i in range(start+1, n):
        length = spot[i] - spot[start]
        if length > l:
            start = i
            cnt += 1
            break
    if i == n-1:
        cnt += 1
        break

print(cnt)