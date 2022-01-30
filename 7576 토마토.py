from copy import deepcopy
import sys, copy
input = sys.stdin.readline

def tomato(box, m, n):
    new_box = copy.deepcopy(box)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if '1' not in box[i]:
                break
            if box[i][j] == '1':
                if j < m-1:   # 오른쪽 이동
                    if new_box[i][j+1] != '1' and box[i][j+1] != '-1':
                        new_box[i][j+1] = '1'
                        cnt += 1
                if j > 0:   # 왼쪽 이동
                    if new_box[i][j-1] != '1'and box[i][j-1] != '-1':
                        new_box[i][j-1] = '1'
                        cnt += 1
                if i < n-1:   # 아래쪽 이동
                    if new_box[i+1][j] != '1'and box[i+1][j] != '-1':
                        new_box[i+1][j] = '1'
                        cnt += 1
                if i > 0:   # 위쪽 이동
                    if new_box[i-1][j] != '1'and box[i-1][j] != '-1':
                        new_box[i-1][j] = '1'
                        cnt += 1
    if cnt == 0:
        return False
    else:
        return new_box


m, n = map(int, input().split())   # 상자 가로 칸 수, 세로 칸 수
box = []
for _ in range(n):
    box.append(input().split())

day = 0   # 토마토가 모두 익을 때까지의 최소 날짜
while True:
    new_box = tomato(box, m, n)
    if not new_box:
        break
    box = new_box
    day += 1

not_all = False   # 토마토 전체가 다 익었는지 확인
for i in range(n):
    if '0' in box[i]:
        not_all = True

if not_all:
    print('-1')
else:
    print(day)