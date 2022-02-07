from collections import deque
import sys
input = sys.stdin.readline

def tomato():
    if not q:
        return
    while q:
        i, j = q.popleft()
        for ni, nj in (i, j+1), (i+1, j), (i, j-1), (i-1, j):
            if 0 <= ni < n and 0 <= nj < m:
                if box[ni][nj] == '0':
                    box[ni][nj] = int(box[i][j]) + 1
                    q.append((ni, nj))
    return int(box[i][j]) - 1

# 입력
m, n = map(int, input().split())   # 상자 가로 칸 수, 세로 칸 수
box = []
q = deque()
for i in range(n):
    box.append(input().split())
    if '1' in box[i]:
        for j in range(m):
            if box[i][j] == '1':
                q.append((i, j))   # 처음 토마토가 익어있는 곳 (1인 곳) 저장

# 출력
result = tomato()
not_all = False
for i in range(n):
    if '0' in box[i]:
        not_all = True   # 전체가 익지 못 함
if not_all:
    print(-1)
else:
    print(result)