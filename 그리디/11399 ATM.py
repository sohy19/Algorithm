import sys
input = sys.stdin.readline

n = int(input())
waiting_time= list(map(int, input().split()))

waiting_time.sort()
time = waiting_time[0]
all_time = 0

for i in range(1, n):
    time += waiting_time[i]
    all_time += time

print(waiting_time[0]+all_time)