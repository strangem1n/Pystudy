import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    lis = [arr[0]]
    for i in range(1, n):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            lis[bisect_left(lis, arr[i])] = arr[i]
    print(len(lis))
