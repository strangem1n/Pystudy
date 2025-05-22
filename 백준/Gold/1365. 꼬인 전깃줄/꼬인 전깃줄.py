import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]
for i in range(1, n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        idx = bisect_left(lis, arr[i])
        lis[idx] = arr[i]
print(n - len(lis))