import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
r = int(input())

adj = [[] for _ in range(n+1)]
stack = []
for i in range(n):
    if i == r or parent[i] == r:
        continue
    if parent[i] == -1:
        stack.append(i)
    adj[parent[i]].append(i)

ans = 0
visited = [False] * (n+1)
while stack:
    node = stack[-1]
    for next_node in adj[node]:
        if not visited[next_node]:
            visited[node] = True
            stack.append(next_node)
            break
    else:
        if not visited[node]:
            ans += 1
            visited[node] = True
        stack.pop()
print(ans)
