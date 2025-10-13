import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    q = deque([(idx, 1)])
    visited = [0] * (n+1)
    while q:
        friend, score = q.popleft()
        if visited[friend] == 0:
            visited[friend] = score
            for next_friend in adj[friend]:
                q.append((next_friend, score + 1))
    return max(visited) - 1

n = int(input())
adj = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)

min_score = n
president = []
for i in range(1, n+1):
    this_score = bfs(i)
    if min_score > this_score:
        min_score = this_score
        president = [i]
    elif min_score == this_score:
        president.append(i)
print(min_score, len(president))
print(*sorted(president))
