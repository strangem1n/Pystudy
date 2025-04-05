import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
        return rep[x]

    else:
        return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

v, e = map(int, input().split())
rep = [i for i in range(v+1)]
adj = [list(map(int, input().split())) for _ in range(e)]
adj.sort(key=lambda x: x[2])

result = 0
for i in range(e):
    n1, n2, cost = adj[i]
    if find_set(n1) != find_set(n2):
        result += cost
        union(n1, n2)
print(result)
