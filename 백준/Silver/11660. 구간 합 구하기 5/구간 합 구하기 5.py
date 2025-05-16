import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]

for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == 1:
        print(arr[x2-1][y2-1])
    elif x1 == 1:
        print(arr[x2-1][y2-1] - arr[x2-1][y1-2])
    elif y1 == 1:
        print(arr[x2-1][y2-1] - arr[x1-2][y2-1])
    else:
        print(arr[x2-1][y2-1] - arr[x1-2][y2-1] - arr[x2-1][y1-2] + arr[x1-2][y1-2])
