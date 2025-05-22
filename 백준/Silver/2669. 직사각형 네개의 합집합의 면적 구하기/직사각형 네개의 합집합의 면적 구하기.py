import sys
input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

result = 0
for x in range(101):
    for y in range(101):
        result += arr[y][x]

print(result)
