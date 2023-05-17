def calc(now):
    if now == n:
        cnt = 1
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                cnt += 1
                if cnt == 3:
                    return
            else:
                cnt = 1
        # if cnt < 3:
        for el in nums:
            print(el, end=" ")
        print()
        return
    for i in range(1, k+1):
        nums.append(i)
        calc(now + 1)
        nums.pop()

k, n = map(int, input().split())
nums = []
calc(0)
