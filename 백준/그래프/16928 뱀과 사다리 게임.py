import sys
from queue import PriorityQueue
input = sys.stdin.readline


def get_num():
    pq = PriorityQueue()
    pq.put((0, 1))   # (주사위 횟수, 위치)
    visited = set() 
    
    while pq:
        num, pos = pq.get()

        for i in range(1, 7):
            move_pos = pos + i

            if move_pos in ladder:
                move_pos = ladder[move_pos]
            if move_pos in snake:
                move_pos = snake[move_pos]

            if move_pos == 100:
                return num + 1
                
            if move_pos < 100 and move_pos not in visited:
                visited.add(move_pos)
                pq.put((num + 1, move_pos))


n, m = map(int, input().split())   # n: 사다리 수, m: 뱀 수
ladder = {k: v for k, v in (map(int, input().split()) for _ in range(n))}   # 사다리 정보
snake = {k: v for k, v in (map(int, input().split()) for _ in range(m))}   # 뱀 정보

print(get_num())
