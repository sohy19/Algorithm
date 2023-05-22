def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def calc_max(i, j, cnt):
    global max_cnt
    for x in range(1, n):
        if arrows[i][j] == 1:
            if in_range(i-x, j) and grid[i][j] < grid[i-x][j]:
                calc_max(i-x, j, cnt+1)
        elif arrows[i][j] == 2:
            if in_range(i-x, j+x) and grid[i][j] < grid[i-x][j+x]:
                calc_max(i-x, j+x, cnt+1)
        elif arrows[i][j] == 3:
            if in_range(i, j+x) and grid[i][j] < grid[i][j+x]:
                calc_max(i, j+x, cnt+1)
        elif arrows[i][j] == 4:
            if in_range(i+x, j+x) and grid[i][j] < grid[i+x][j+x]:
                calc_max(i+x, j+x, cnt+1)
        elif arrows[i][j] == 5:
            if in_range(i+x, j) and grid[i][j] < grid[i+x][j]:
                calc_max(i+x, j, cnt+1)
        elif arrows[i][j] == 6:
            if in_range(i+x, j-x) and grid[i][j] < grid[i+x][j-x]:
                calc_max(i+x, j-x, cnt+1)
        elif arrows[i][j] == 7:
            if in_range(i, j-x) and grid[i][j] < grid[i][j-x]:
                calc_max(i, j-x, cnt+1)
        elif arrows[i][j] == 8:
            if in_range(i-x, j-x) and grid[i][j] < grid[i-x][j-x]:
                calc_max(i-x, j-x, cnt+1)
    max_cnt = max(cnt, max_cnt)
    return

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arrows = [list(map(int, input().split())) for _ in range(n)]
start = list(map(int, input().split()))
max_cnt = 0
calc_max(start[0]-1, start[1] - 1, 0)
print(max_cnt)
