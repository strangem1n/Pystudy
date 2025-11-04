import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xi, yi = find(x), find(y)
    if xi > yi:
        parent[xi] = yi
    else:
        parent[yi] = xi

n, q = map(int, input().split())
parent = [i for i in range(n+1)]
vertex = []
for _ in range(q):
    s, e, c, t = map(int, input().split())
    heapq.heappush(vertex, (c, t, s, e))

cost = time = cnt = 0
while cnt != n-1 and vertex:
    c, t, s, e = heapq.heappop(vertex)
    if find(s) != find(e):
        union(s, e)
        cost += c
        cnt += 1
        if time < t:
            time = t
if cnt == n-1:
    print(time, cost)
else:
    print(-1)
