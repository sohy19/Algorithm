def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def moving():
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    dir_num = 1
    x, y = 0, -1
    for i in range(1, n*n+1):
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if not in_range(nx, ny) or grid[nx][ny] != 0:
            dir_num = (dir_num + 1) % 4
        x, y = x + dx[dir_num], y + dy[dir_num]
        grid[x][y] = i


T = int(input())
for t in range(1, T+1):
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    moving()
    print(f"#{t}")
    for i in range(n):
        print(*grid[i])
