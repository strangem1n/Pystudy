import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)
q = deque([])
level = [0] * (n+1)
adj = [None] * (n+1)
for i in range(1, n+1):
    cost, *prev, end = map(int, input().split())
    arr[i] = cost
    adj[i] = prev
    level[i] = len(prev)


for i in range(1, n+1):
        if level[i] == 0:
            q.append(i)

order = deque([])
while q:
    v = q.popleft()
    for i in range(1, n+1):
        if v in adj[i]:
            level[i] -= 1
            if level[i] == 0:
                q.append(i)
    order.append(v)

result = [0] * (n+1)
before = [0] * (n+1)
while order:
    i = order.popleft()
    result[i] = arr[i] + before[i]
    for j in range(1, n+1):
        if i in adj[j]:
            before[j] = max(before[j], result[i])

for i in range(1, n+1):
    print(result[i])