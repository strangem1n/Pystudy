import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]
for i in range(1, n):
    if arr[i] >= result[-1]:
        result.append(arr[i])
    else:
        j = bisect_left(result, arr[i])
        result[j] = arr[i]
print(len(result))