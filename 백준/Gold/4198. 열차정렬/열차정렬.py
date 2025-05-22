import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

max_len = 0
for i in range(n):
    start = arr[i]

    lis = [start]
    for j in range(i+1, n):
        if lis[-1] < arr[j]:
            lis.append(arr[j])
        else:
            idx = bisect_left(lis, arr[j])
            if idx == 0:
                continue
            lis[idx] = arr[j]

    lds = [-start]
    for j in range(i+1, n):
        if lds[-1] < -arr[j]:
            lds.append(-arr[j])
        else:
            idx = bisect_left(lds, -arr[j])
            if idx == 0:
                continue
            lds[idx] = -arr[j]

    train_len = len(lis) + len(lds) - 1
    if max_len < train_len:
        max_len = train_len

print(max_len)