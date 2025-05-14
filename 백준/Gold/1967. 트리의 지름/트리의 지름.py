import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(start, dist):
    v = adj[start]
    max_dist = dist
    for cost, node in v:
        if not visited[node]:
            visited[node] = True
            max_dist = max(max_dist, dfs(node, dist+cost))
            visited[node] = False
    return max_dist

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

root = []
for i in range(1, n+1):
    if len(adj[i]) == 1:
        root.append(i)

max_length = 0
visited = [False] * (n+1)
for r in root:
    visited[r] = 1
    max_length = max(max_length, dfs(r, 0))
    visited[r] = 0
print(max_length)
