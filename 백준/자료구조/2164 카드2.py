from collections import deque

n = int(input())
queue = deque([i+1 for i in range(n)])

ch = 1  # 어떤 동작 해야 하는지 표시 (1: 제일 위에 있는 카드 제거, 2: 제일 위에 있는 카드 맨 밑으로)
cnt = n
while cnt != 1:
    if ch == 1:
        queue.popleft()
        ch = 2
        cnt -= 1
    elif ch == 2:
        queue.append(queue.popleft())
        ch = 1

print(queue[0])
