import sys, heapq
input = sys.stdin.readline

def dijk():
    pq = []
    dist = [[] for _ in range(n+1)]
    heapq.heappush(pq, (0, 1))
    while pq:
        cost, node = heapq.heappop(pq)
        if len(dist[node]) >= k:
            max_cost = -heapq.heappop(dist[node])
            if cost >= max_cost:
                heapq.heappush(dist[node], -max_cost)
                continue
        heapq.heappush(dist[node], -cost)
        for next_cost, next_node in adj[node]:
            heapq.heappush(pq, (cost+next_cost, next_node))

    for i in range(1, n+1):
        d = dist[i]
        if len(d) < k:
            print(-1)
        else:
            print(-d[0])


n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
dijk()
