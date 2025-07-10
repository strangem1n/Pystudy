import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
level = [0] * (n+1)

for _ in range(m):
    k, *nodes = map(int, input().split())
    for i in range(k):
        for j in range(i+1, k):
            if nodes[i] not in adj[nodes[j]]:
                adj[nodes[j]].append(nodes[i])
                level[nodes[j]] += 1

q = deque([])
for i in range(1, n+1):
    if level[i] == 0:
        q.append(i)

result = []
while q:
    prev = q.popleft()
    for i in range(1, n+1):
        if prev in adj[i]:
            level[i] -= 1
            if level[i] == 0:
                q.append(i)
    result.append(prev)

if len(result) == n:
    for r in result:
        print(r)
else:
    print(0)