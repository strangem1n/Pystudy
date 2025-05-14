import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(lambda x: -int(x), input().split()))
ans = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > ans[-1]:
        ans.append(arr[i])
    else:
        pos = bisect_left(ans, arr[i])
        ans[pos] = arr[i]
print(len(ans))