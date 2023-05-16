
def calc():
    if 1 not in flag:
        return 0
    last = -1
    cnt = 0
    for i in range(n):
        if flag[i]:
            if last == -1:
                last = lines[i][1]
                cnt += 1
            else:
                if last < lines[i][0]:
                    last = lines[i][1]
                    cnt += 1
    return cnt

def including_line(now, most_cnt):
    if now == n:
        cnt = calc()
        if most_cnt < cnt:
            most_cnt = cnt
        return most_cnt
    for i in range(2):
        flag.append(i)
        most_cnt = including_line(now + 1, most_cnt)
        flag.pop()
    return most_cnt

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
flag = []   # 선 포함 시키는지 안 시키는지 표시
print(including_line(0, 0))
