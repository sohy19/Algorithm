import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().strip()
    k = int(input())
    min_len = sys.maxsize
    max_len = 0

    dict = {}

    for i in range(len(string)):
        s = string[i]
        if s in dict:
            dict[s].append(i)
        else:
            dict[s] = [i]

        if len(dict[s]) >= k:
            length = dict[s][len(dict[s]) - 1] - dict[s][len(dict[s]) - k] + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)
        
        
    if min_len == sys.maxsize:
        print(-1)
    else:
        print(min_len, max_len)
