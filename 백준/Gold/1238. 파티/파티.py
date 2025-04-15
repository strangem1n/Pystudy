import sys,heapq
input = sys.stdin.readline


def dijkstra(start, end):
    dist = [float('inf')] * (n+1)
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        for next_cost, new_node in adj[node]:
            new_cost = cost + next_cost
            if dist[new_node] <= new_cost:
                continue
            heapq.heappush(pq, (new_cost, new_node))
    return dist[end]


n, m, x = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])

max_t = 0
for i in range(1, n+1):
    t = dijkstra(i, x) + dijkstra(x, i)
    if max_t < t:
        max_t = t
print(max_t)
