import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if arr[0] > -1:
    print(*arr[:3])
elif arr[-1] < 1:
    print(*arr[-3:])
else:
    min_diff = float('inf')
    min_list = [0] * 3
    for i in range(n):
        a = arr[i]
        for j in range(n):
            if i == j:
                continue
            b = arr[j]
            k = bisect_left(arr, -(a+b), 0, n-1)
            if arr[k] != -(a+b):
                if 0 < k and i != k-1 and j != k-1:
                    c = arr[k-1]
                    diff = abs(a+b+c)
                    if min_diff > diff:
                        min_diff = diff
                        min_list = [a, b, c]
                if k < n-1 and i != k+1 and j != k+1:
                    c = arr[k+1]
                    diff = abs(a + b + c)
                    if min_diff > diff:
                        min_diff = diff
                        min_list = [a, b, c]
            if i != k and j != k:
                c = arr[k]
                diff = abs(a+b+c)
                if min_diff > diff:
                    min_diff = diff
                    min_list = [a, b, c]
        if min_diff == 0:
            break
    min_list.sort()
    print(*min_list)
