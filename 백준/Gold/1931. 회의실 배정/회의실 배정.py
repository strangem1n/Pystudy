import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
result = 1
start, end = arr[0]
idx = 1
while idx < n:
    if end <= arr[idx][0]:
        result += 1
        start, end = arr[idx]
    idx += 1
print(result)
