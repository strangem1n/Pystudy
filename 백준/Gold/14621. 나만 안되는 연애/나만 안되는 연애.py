import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
        return parent[x]
    else:
        return x


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
college = [0] + list(map(lambda x: 0 if x == 'M' else 1, input().split()))
parent = [i for i in range(n+1)]
adj = []

for _ in range(m):
    u, v, d = map(int, input().split())
    if college[u] == college[v]:
        continue
    adj.append([d, u, v])
adj.sort()

mst = 0
cnt = 0
for d, u, v in adj:
    if cnt == n-1:
        break
    if find_set(u) != find_set(v):
        union(u, v)
        mst += d
        cnt += 1
if cnt == n-1:
    print(mst)
else:
    print(-1)
