x = int(input())
dp = [0 for i in range(x+1)]

for i in range(2, x+1):
    if i ==2 or i ==3:    # 초기화
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[int(i/3)] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[int(i/2)] + 1)          

print(dp[-1])
