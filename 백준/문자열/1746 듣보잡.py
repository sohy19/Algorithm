import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n: 듣도 못한 사람의 수, m: 보도 못한 사람의 수
not_listen = [input().strip() for _ in range(n)]
not_see = [input().strip() for _ in range(m)]

dic = {}
not_listen_see = []   # 듣보잡 리스트
cnt = 0   # 듣보잡 수
for i in range(n):
    dic[not_listen[i]] = 1

for i in range(m):
    if not_see[i] in dic:
        not_listen_see.append(not_see[i])
        cnt += 1
not_listen_see.sort()

print(cnt)
for i in range(cnt):
    print(not_listen_see[i])