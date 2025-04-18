import sys
input = sys.stdin.readline

n = int(input())
triangle = [[0] * n for _ in range(n)]

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(i+1):
        triangle[i][j] = num[j]

for i in range(1, n):
    for j in range(i+1):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))
