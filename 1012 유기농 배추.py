import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(g, x, y, m, n):
    g[x][y] = (1, True)
    if y < m-1:   # 오른쪽 이동
        if g[x][y+1] == (1, False):
            dfs(g, x, y+1, m, n)
    if y > 0:   # 왼쪽 이동
        if g[x][y-1] == (1, False):
            dfs(g, x, y-1, m, n)
    if x < n-1:   # 아래쪽 이동
        if g[x+1][y] == (1, False):
            dfs(g, x+1, y, m, n)
    if x > 0:   # 위쪽 이동
        if g[x-1][y] == (1, False):
            dfs(g, x-1, y, m, n)
    return True

worm = []   # 지렁이 수
test_case = int(input())
for _ in range(test_case):
    count = 0
    m, n, k = map(int, input().split())   # 가로 길이, 세로 길이, 배추 위치 개수
    g = [[(0, False) for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        g[x][y] = (1, False)
    for i in range(n):
        for j in range(m):
            if g[i][j] == (1, False):
                dfs(g, i, j, m, n)
                count +=1
    worm.append(count)

for i in range(test_case):
    print(worm[i])
