import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
arr.append([10**9+1, 10**9+2])

s, e = arr[0]
ans = 0
for i in range(1, n+1):
    if e >= arr[i][0]:
        e = max(e, arr[i][1])
    else:
        ans += e - s
        s, e = arr[i]
print(ans)
