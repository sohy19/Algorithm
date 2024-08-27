n = int(input())
for _ in range(n):
    re, char = input().split()
    re = int(re)
    for ch in char:
        print(ch * re, end='')
    print()
