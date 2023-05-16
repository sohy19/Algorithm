def print_num():
    for el in nums:
        print(el, end=" ")
    print()

def choose_num(now):
    if now == n + 1:
        print_num()
        return
    for i in range(1, k+1):
        nums.append(i)
        choose_num(now+1)
        nums.pop()

k, n = map(int, input().split())
nums = []
choose_num(1)
