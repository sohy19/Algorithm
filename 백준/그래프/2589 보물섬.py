import sys
input = sys.stdin.readline

def treasure(start_y, start_x):
    queue = [(start_y, start_x)]
    visited = [[0 for _ in range(width)] for _ in range(height)]
    visited[start_y][start_x] = 1
    max_time = 0   # 최단 거리로 이동하는 최대 시간
    while queue:
        i, j = queue.pop(0)
        for w, z in (i+1, j), (i, j+1), (i, j-1), (i-1, j):
            if 0 <= w < height and 0 <= z < width:
                if treasure_map[w][z] == "L" and visited[w][z] == 0:
                    visited[w][z] = visited[i][j] + 1
                    queue.append((w, z))
                    max_time = max(max_time, visited[w][z])
    return max_time - 1

# 입력
height, width = map(int, input().split())
treasure_map = []
for _ in range(height):
    treasure_map.append(input())

# 출력
max_time = 0
for i in range(height):
    for j in range(width):
        if treasure_map[i][j] == "L":
            max_time = max(max_time, treasure(i, j))
print(max_time)