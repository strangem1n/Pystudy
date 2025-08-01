import sys, heapq
input = sys.stdin.readline

def find(x):
    if ref[x] != x:
        ref[x] = find(ref[x])
        return ref[x]
    else:
        return x

def union(x, y):
    if find(x) > find(y):
        x, y = y, x
    ref[find(y)] = find(ref[x])


n, m = map(int, input().split())
ref = [i for i in range(n+1)]
pq = []
for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, [c, a, b])

result = 0
last_cost = 0
cnt = 0
while pq and cnt < n-1:
    cost, h1, h2 = heapq.heappop(pq)
    if find(h1) != find(h2):
        union(h1, h2)
        result += cost
        last_cost = cost
        cnt += 1
result -= last_cost
print(result)