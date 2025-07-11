import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
level = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    level[b] += 1

q = deque([])
for i in range(1, n+1):
    if level[i] == 0:
        q.append(i)

while q:
    front = q.popleft()
    for back in adj[front]:
        level[back] -= 1
        if level[back] == 0:
            q.append(back)
    print(front, end=' ')