import sys
input = sys.stdin.readline

def knight_move(start_x, start_y, finish_x, finish_y, m):
    queue = [(start_x, start_y)]
    chess = [[0 for _ in range(m)] for _ in range(m)]
    chess[start_x][start_y] = 1
    while queue:
        i, j = queue.pop(0)
        if i == finish_x and j == finish_y:
            return chess[i][j] - 1
        for w, z in [(i+2, j+1), (i+1, j+2), (i+2, j-1), (i+1, j-2), (i-2, j+1), (i-1, j+2), (i-2, j-1), (i-1, j-2)]:         
            if w < m and z < m and w >= 0 and z >= 0:
                if chess[w][z] != 0:
                    continue   
                chess[w][z] = chess[i][j] + 1
                queue.append((w, z))

test_case = int(input())
result = []   # 결과 저장
for _ in range(test_case):
    m = int(input())   # 한 변의 길이
    start_x, start_y = map(int, input().split())   # 나이트가 현재 잇는 칸
    finish_x, finish_y = map(int, input().split())   # 나이트가 이동하려고 하는 칸
    result.append(knight_move(start_x, start_y, finish_x, finish_y, m))

for i in range(test_case):
    print(result[i])