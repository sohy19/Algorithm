import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
red_dp = [[0] * 3 for _ in range(n)]
green_dp = [[0] * 3 for _ in range(n)]
blue_dp = [[0] * 3 for _ in range(n)]


red_dp[1][0] = sys.maxsize
red_dp[1][1] = cost[1][1] + cost[0][0]
red_dp[1][2] = cost[1][2] + cost[0][0]
green_dp[1][0] = cost[1][0] + cost[0][1]
green_dp[1][1] = sys.maxsize
green_dp[1][2] = cost[1][2] + cost[0][1]
blue_dp[1][0] = cost[1][0] + cost[0][2]
blue_dp[1][1] = cost[1][1] + cost[0][2]
blue_dp[1][2] = sys.maxsize

for i in range(2, n):
      if i == n-1:
        red_dp[i][0] = sys.maxsize
        red_dp[i][1] = cost[i][1] + min(red_dp[i-1][0], red_dp[i-1][2])
        red_dp[i][2] = cost[i][2] + min(red_dp[i-1][0], red_dp[i-1][1])

        green_dp[i][0] = cost[i][0] + min(green_dp[i-1][1], green_dp[i-1][2])
        green_dp[i][1] = sys.maxsize
        green_dp[i][2] = cost[i][2] + min(green_dp[i-1][0], green_dp[i-1][1])

        blue_dp[i][0] = cost[i][0] + min(blue_dp[i-1][1], blue_dp[i-1][2])
        blue_dp[i][1] = cost[i][1] + min(blue_dp[i-1][0], blue_dp[i-1][2])
        blue_dp[i][2] = sys.maxsize

      else:
        red_dp[i][0] = cost[i][0] + min(red_dp[i-1][1], red_dp[i-1][2])
        red_dp[i][1] = cost[i][1] + min(red_dp[i-1][0], red_dp[i-1][2])
        red_dp[i][2] = cost[i][2] + min(red_dp[i-1][0], red_dp[i-1][1])
        
        green_dp[i][0] = cost[i][0] + min(green_dp[i-1][1], green_dp[i-1][2])
        green_dp[i][1] = cost[i][1] + min(green_dp[i-1][0], green_dp[i-1][2])
        green_dp[i][2] = cost[i][2] + min(green_dp[i-1][0], green_dp[i-1][1])

        blue_dp[i][0] = cost[i][0] + min(blue_dp[i-1][1], blue_dp[i-1][2])
        blue_dp[i][1] = cost[i][1] + min(blue_dp[i-1][0], blue_dp[i-1][2])
        blue_dp[i][2] = cost[i][2] + min(blue_dp[i-1][0], blue_dp[i-1][1])


print(min(red_dp[n-1] + green_dp[n-1] + blue_dp[n-1]))
