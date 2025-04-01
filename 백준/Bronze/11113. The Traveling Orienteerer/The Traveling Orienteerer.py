n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(float, input().split())
m = int(input())
for _ in range(m):
    track = 0
    p = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, p):
        track += ((x[arr[i]] - x[arr[i-1]]) ** 2 + (y[arr[i]] - y[arr[i-1]]) ** 2) ** (1/2)
    print(round(track))
