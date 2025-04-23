import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
        return parent[x]
    else:
        return x


def union(x, y):
    i = find_set(x)
    j = find_set(y)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
adj = [list(map(int, input().split())) for _ in range(m)]
adj.sort(key=lambda x: x[2])

cnt = 0
reduce_cost = 0
for a, b, c in adj:
    if find_set(a) != find_set(b):
        union(a, b)
        cnt += 1
    else:
        reduce_cost += c

if cnt == n-1:
    print(reduce_cost)
else:
    print(-1)
