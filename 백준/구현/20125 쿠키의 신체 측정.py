import sys
input = sys.stdin.readline

N = int(input())
cookie = [input().strip() for _ in range(N)]

def calc_len(x, y, dir_num):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽
    length = 0
    while cookie[x][y] == "*":
        length += 1
        x += dir[dir_num][0]
        y += dir[dir_num][1]

        if not (0 <= x < N and 0 <= y < N):
            break

    return length

def get_cookie():
    for i in range(N):
        for j in range(N):
            if cookie[i][j] == "*":
                heart_x, heart_y = i + 1, j
                left_arm = calc_len(heart_x, heart_y-1, 2)   # 왼쪽 팔
                right_arm = calc_len(heart_x, heart_y+1, 3)   # 오른쪽 팔
                waist = calc_len(heart_x+1, heart_y, 1)   # 허리
                left_leg = calc_len(heart_x+waist+1, heart_y-1, 1)   # 왼쪽 다리
                right_leg = calc_len(heart_x+waist+1, heart_y+1, 1)   # 오른쪽 다리
                print(heart_x+1, heart_y+1)
                print(left_arm, right_arm, waist, left_leg, right_leg)
                return
    
get_cookie()
