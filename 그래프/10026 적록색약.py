import sys, copy
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_section(color, n, now_row, now_col, visited):
    visited[now_row][now_col] = True
    if now_col < n-1:   # 오른쪽 이동
        if color[now_row][now_col] == color[now_row][now_col+1] and not visited[now_row][now_col+1]:
            find_section(color, n, now_row, now_col+1, visited)
    if now_col > 0:   # 왼쪽 이동
        if color[now_row][now_col] == color[now_row][now_col-1] and not visited[now_row][now_col-1]:
            find_section(color, n, now_row, now_col-1, visited)
    if now_row < n-1:   # 아래쪽 이동
        if color[now_row][now_col] == color[now_row+1][now_col] and not visited[now_row+1][now_col]:
            find_section(color, n, now_row+1, now_col, visited)
    if now_row > 0:   # 위쪽 이동
        if color[now_row][now_col] == color[now_row-1][now_col] and not visited[now_row-1][now_col]:
            find_section(color, n, now_row-1, now_col, visited)
    return True

n = int(input())
color = []
for _ in range(n):
    color.append(input().strip())

w_color = copy.deepcopy(color)   # 적록색약인 사람이 보는 색
for i in range(n):
    if 'G' in w_color[i]:
        w_color[i] = w_color[i].replace('G', 'R')
        
visited = [[False for _ in range(n)] for _ in range(n)]
w_visited = [[False for _ in range(n)] for _ in range(n)]
section = 0
w_section = 0   # 적록색약인 사람이 보는 구역 개수

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            find_section(color, n, i, j, visited)
            section += 1
        if w_visited[i][j] == False:
            find_section(w_color, n, i, j, w_visited)
            w_section += 1

print(section, w_section)