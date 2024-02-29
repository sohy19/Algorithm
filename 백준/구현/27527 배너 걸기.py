import math

n, m = map(int, input().split())
space = list(map(int, input().split()))
num = math.ceil((9 * m) / 10)
count = 0
height = {}
flag = False

for i in range(n):
    # 추가
    if space[i] in height:
        height[space[i]] += 1
    else:
        height[space[i]] = 1
    
    # 삭제
    if i >= m:
        height[space[i-m]] -= 1
    
    # 개수가 넘는지 확인
    if height[space[i]] >= num:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
