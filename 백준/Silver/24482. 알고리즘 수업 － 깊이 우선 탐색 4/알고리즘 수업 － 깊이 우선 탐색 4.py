import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(root):
    for next_node in adj[root]:
        if visited[next_node] == -1:
            visited[next_node] = visited[root]+1
            dfs(next_node)


n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
for a in adj:
    a.sort(reverse=True)

visited = [-1] * (n+1)
visited[r] = 0
dfs(r)
for i in range(1, n+1):
    print(visited[i])
