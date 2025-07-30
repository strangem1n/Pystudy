import sys
input = sys.stdin.readline

def solve(color):
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][color] = arr[0][color]
    dp[0][(color+1)%3] = dp[0][(color+2)%3] = float('inf')
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + arr[i][j]
    return min(dp[n-1][(color+1)%3], dp[n-1][(color+2)%3])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_cost = float('inf')
for k in range(3):
    cost = solve(k)
    if min_cost > cost:
        min_cost = cost
print(min_cost)