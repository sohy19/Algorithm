def calc_score():
    score = 0
    for el in targets:
        if sum(el) + 1 >= m:
            score += 1
    return score

def calc(now):
    global max_score
    if now == n:
        score = calc_score()
        if max_score < score:
            max_score = score
        return
    for i in range(k):
        targets[i].append(move[now])
        calc(now + 1)
        targets[i].pop()


n, m, k = map(int, input().split())
move = list(map(int, input().split()))
targets = [[] for _ in range(k)]
max_score = 0
calc(0)
print(max_score)
