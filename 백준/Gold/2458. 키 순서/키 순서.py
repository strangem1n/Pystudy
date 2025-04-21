import sys
input = sys.stdin.readline


def dfs(num, typ):
    visited = [0] * (n+1)
    visited[num] = 1
    stack = [num]
    if typ == 1:
        adj = adj_pos
    else:
        adj = adj_neg

    while stack:
        node = stack[-1]
        for next_node in adj[node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                stack.append(next_node)
                break
        else:
            stack.pop()

    cnt = -1
    for i in range(n+1):
        if visited[i] == 1:
            cnt += 1
    return cnt


n, m = map(int, input().split())
adj_pos = [[] for _ in range(n+1)]
adj_neg = [[] for _ in range(n+1)]

for _ in range(m):
    short, tall = map(int, input().split())
    adj_pos[short].append(tall)
    adj_neg[tall].append(short)

result = 0
for i in range(1, n+1):
    if dfs(i, 1) + dfs(i, 0) == n-1:
        result += 1
print(result)
