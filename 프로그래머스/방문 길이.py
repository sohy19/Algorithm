def in_range(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5

def solution(dirs):
    x, y = 0, 0
    dic = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
    trace = set()
    answer = 0
    for d in dirs:
        dx, dy = x + dic[d][0], y + dic[d][1]
        if in_range(dx, dy):
            if not ((x, y, dx, dy) in trace or (dx, dy, x, y) in trace):
                trace.add((x, y, dx, dy))
                answer += 1
            x, y = dx, dy
    print(answer)            
    return answer
