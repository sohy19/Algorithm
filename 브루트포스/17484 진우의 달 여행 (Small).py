import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dir = {1: (1, -1), 2: (1, 0), 3: (1, 1)}

def dfs(i, j, now_dir, min_fuel, fuel):
    if i == n-1:
        return min(min_fuel, fuel)
    for k in range(1, 4):
        if now_dir != k:
            if 0 <= i+dir[k][0] < n and 0 <= j+dir[k][1] < m:
                min_fuel = dfs(i+dir[k][0], j+dir[k][1], k, min_fuel, fuel+grid[i+dir[k][0]][j+dir[k][1]])
    return min_fuel

min_fuel = int(sys.maxsize)
for i in range(m):
    min_fuel = min(dfs(0, i, 0, min_fuel, grid[0][i]), min_fuel)

print(min_fuel)
