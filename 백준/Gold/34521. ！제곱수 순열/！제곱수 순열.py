import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    power = 3
    ans = [i for i in range(1, n+1)]
    idx = 0
    while idx < n-1:
        if ans[idx] + ans[idx + 1] == power ** 2:
            ans[idx], ans[idx - 1] = ans[idx - 1], ans[idx]
            idx -= 1
        elif ans[idx] + ans[idx + 1] > power ** 2:
            power += 1
        else:
            idx += 1
    print(*ans)