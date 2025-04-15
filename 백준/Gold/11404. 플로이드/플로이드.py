import sys
input = sys.stdin.readline

n = int(input())
bus = int(input())
arr = [[float('inf')] * n for _ in range(n)]
for _ in range(bus):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0

for a in arr:
    print(*a)
