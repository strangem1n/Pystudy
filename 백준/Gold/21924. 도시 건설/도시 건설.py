import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
        return parent[x]
    else:
        return x


def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
adj = [list(map(int, input().split())) for _ in range(m)]
adj.sort(key=lambda x: x[2])

cnt = 0
reduce_cost = 0
for a, b, c in adj:
    a1 = find_set(a)
    b1 = find_set(b)
    if a1 != b1:
        union(a1, b1)
        cnt += 1
    else:
        reduce_cost += c

if cnt == n-1:
    print(reduce_cost)
else:
    print(-1)
