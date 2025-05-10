import sys, heapq
input = sys.stdin.readline

def dijk(start):
    dist = [float('inf')] * (n+1)
    hq = []
    heapq.heappush(hq, [0, start])
    item = 0
    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] <= cost:
            continue
        if cost > m:
            continue
        dist[node] = cost
        item += items[node-1]
        for next_cost, next_node in adj[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            heapq.heappush(hq, [cost+next_cost, next_node])
    return item

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    adj[a].append([l, b])
    adj[b].append([l, a])

max_item = 0
for i in range(1, n):
    max_item = max(max_item, dijk(i))
print(max_item)
