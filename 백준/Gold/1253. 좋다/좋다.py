import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(n):
    target = arr[i]
    for j in range(n):
        if i != j:
            a = arr[j]
            b = target - a
            k = bisect_left(arr, b)
            l = bisect_right(arr, b)-1
            if 0 <= k < n and k != i and k != j and arr[k] == b:
                result += 1
                break
            if 0 <= l < n and l != i and l != j and arr[l] == b:
                result += 1
                break
print(result)
