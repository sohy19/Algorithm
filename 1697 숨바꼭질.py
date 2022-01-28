import sys
input = sys.stdin.readline

n, k = map(int, input().split())   # 수빈이 위치, 동생 위치
sec = [0 for _ in range(100001)]    # 동생을 찾는 가장 빠른 시간
queue = [n]
while queue:
    u = queue.pop(0)
    if u == k:
        break
    for w in [u-1, u+1, u*2]:
        if w < 0 or w > 100000 or w == n:
            continue
        if sec[w] == 0:   # 시간이 0인 것은 아직 방문하지 않은 것
            sec[w] = sec[u] + 1
            queue.append(w)

print(sec[k])