import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def moving(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and visited[bord[nx][ny]] == 0:
            visited[bord[nx][ny]] = 1
            moving(nx, ny, cnt+1)
            visited[bord[nx][ny]] = 0

r, c = map(int, input().split())   # 세로 R, 가로 C
bord = [list(map(lambda a : ord(a)-65, input())) for _ in range(r)]
visited = [0] * 26
visited[bord[0][0]] = 1
max_cnt = 0
moving(0, 0, 1)
print(max_cnt)