import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > ans[-1]:
        ans.append(arr[i])
    else:
        ans[bisect_left(ans, arr[i])] = arr[i]

print(len(ans))
