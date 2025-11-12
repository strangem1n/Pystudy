import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(init):
    q = deque([(init, 0)])
    visit = defaultdict(bool)
    visit[init] = True
    while q:
        a, cnt = q.popleft()
        if a == ans:
            return cnt
        for i in range(n-k+1):
            na = a[:i] + a[i:i+k][::-1] + a[i+k:]
            if visit[na]:
                continue
            visit[na] = True
            q.append((na, cnt+1))
    return -1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = "".join(map(str, sorted(arr)))
print(bfs("".join(map(str, arr))))
