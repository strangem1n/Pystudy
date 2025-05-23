import sys, heapq
input = sys.stdin.readline

def dijk(road):
    dist = [[float('inf')] * (road+1) for _ in range(n+1)]
    pq = []
    heapq.heappush(pq, (0, 1, road))
    while pq:
        cost, node, left_road = heapq.heappop(pq)
        if dist[node][left_road] <= cost:
            continue
        dist[node][left_road] = cost
        for next_cost, next_node in adj[node]:
            if left_road > 0 and dist[next_node][left_road-1] > cost:
                heapq.heappush(pq, (cost, next_node, left_road-1))
            if dist[next_node][left_road] > cost+next_cost:
                heapq.heappush(pq, (cost+next_cost, next_node, left_road))
    return min(dist[n])

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
print(dijk(k))