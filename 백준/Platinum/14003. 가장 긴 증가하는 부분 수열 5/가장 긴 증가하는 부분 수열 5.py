import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]
record = [0] * n

for i in range(1, len(arr)):
    if arr[i] > ans[-1]:
        ans.append(arr[i])
        record[i] = len(ans) - 1
    else:
        pos = bisect_left(ans, arr[i])
        ans[pos] = arr[i]
        record[i] = pos

l = len(ans) - 1
idx = -1
while l > -1:
    if record[idx] == l:
        ans[l] = arr[idx]
        l -= 1
    idx -= 1

print(len(ans))
print(*ans)
