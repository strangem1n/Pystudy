import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]
memo[0][0] = 1

for j in range(n):
    i = 0
    while j >= 0:
        if memo[i][j] > 0 and arr[i][j] > 0:
            ni = i + arr[i][j]
            nj = j + arr[i][j]
            if 0 <= ni < n:
                memo[ni][j] += memo[i][j]
            if 0 <= nj < n:
                memo[i][nj] += memo[i][j]
        i += 1
        j -= 1

for i in range(1, n):
    j = n - 1
    while i < n:
        if memo[i][j] > 0 and arr[i][j] > 0:
            ni = i + arr[i][j]
            nj = j + arr[i][j]
            if 0 <= ni < n:
                memo[ni][j] += memo[i][j]
            if 0 <= nj < n:
                memo[i][nj] += memo[i][j]
        i += 1
        j -= 1

print(memo[n-1][n-1])
