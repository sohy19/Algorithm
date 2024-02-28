n = int(input())
nums = list(map(int, input().split()))

nums.sort()
cnt = 0
for i in range(n):
    left = 0
    right = n-1

    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        elif nums[left] + nums[right] == nums[i]:
            cnt += 1
            break
        elif nums[left] + nums[right] < nums[i]:
            left += 1
        else:
            right -= 1
            
print(cnt)
