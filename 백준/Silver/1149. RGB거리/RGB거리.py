house = int(input())
cost = [list(map(int, input().split())) for _ in range(house)]

dp = [[0, 0, 0] for i in range(house)]

for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, house):
    for j in range(3):
        dp[i][j] = cost[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

print(min(dp[house-1]))
