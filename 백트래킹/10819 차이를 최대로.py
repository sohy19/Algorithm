import sys, copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calculate_max(x, arr):
    global max_sum
    result = 0
    sorted_arr = copy.deepcopy(arr)
    for i in range(1, n-x):
        temp = sorted_arr[x]
        sorted_arr[x] = sorted_arr[x+i]
        sorted_arr[x+i] = temp
        calculate_max(x+1, sorted_arr)
    for i in range(1, n):
        result += abs(arr[i] - arr[i-1])
    max_sum = max(max_sum, result)

n = int(input())
arr = list(map(int, input().split()))
max_sum = 0   # 차이가 최대인 값

for i in range(n-2, -1, -1):
    calculate_max(i, copy.deepcopy(arr))

print(max_sum)