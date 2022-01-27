import sys
input = sys.stdin.readline

computer_num = int(input())   # 컴퓨터 수
edge_num = int(input())   # 네트워크 상 직접 연결되어 있는 컴퓨터 번호 쌍
computer = [[] for _ in range(computer_num+1)]
for _ in range(edge_num):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

visited = [False for _ in range(computer_num+1)]
visited[1] = True
count = 0   # 바이러스 걸리게 되는 컴퓨터 수
Q = [1]
while len(Q) != 0:
    u = Q.pop(0)
    for w in computer[u]:
        if visited[w] == False:
            visited[w] = True
            Q.append(w)
            count += 1
        
print(count)