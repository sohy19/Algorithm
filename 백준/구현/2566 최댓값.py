nums = [list(map(int, input().split())) for _ in range(9)]
max_num = x = y = 0

for i in range(9):
    for j in range(9):
        if max_num < nums[i][j]:
            max_num = nums[i][j]
            x = i
            y = j

print(max_num)
print(x+1, y+1)
