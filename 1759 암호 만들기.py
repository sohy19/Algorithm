import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def check_condition(arr):   # 모음 한 개 이상, 자음 두 개 이상 조건이 맞는지 체크
    if not len(arr) == l:
        return False
    vowel, consonant = 0, 0
    for s in arr:
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
            vowel += 1
        else:
            consonant += 1
    return 1 <= vowel and 2 <= consonant

def count(now, arr):
    if not len(arr) == l:
        for i in range(now, len(arr)):
            x = arr.pop(i)
            count(i, arr)
            arr.insert(i, x)
    if check_condition(arr):
        result.append("".join(arr))

l, c = map(int, input().split())
arr = input().split()
result = []
arr.sort()
count(0, arr)
for i in range(len(result)-1, -1, -1):
    print(result[i])