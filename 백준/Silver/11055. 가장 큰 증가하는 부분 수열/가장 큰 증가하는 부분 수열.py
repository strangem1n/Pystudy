import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    max_dp = 0
    for j in range(i):
        if arr[j] < arr[i] and max_dp < dp[j]:
            max_dp = dp[j]
    dp[i] = arr[i] + max_dp
print(max(dp))
