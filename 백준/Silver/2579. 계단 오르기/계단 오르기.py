n = int(input())
stair = list(int(input()) for _ in range(n))

dp = [0] * n
dp[0] = stair[0]
if n > 1:
    dp[1] = stair[0] + stair[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
print(dp[-1])
