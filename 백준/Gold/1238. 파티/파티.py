import sys,heapq
input = sys.stdin.readline


def dijkstra(direction):
    dist = [float('inf')] * (n+1)
    pq = []
    heapq.heappush(pq, (0, x))
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        if direction == 1:
            for next_cost, new_node in adj_for[node]:
                new_cost = cost + next_cost
                if dist[new_node] <= new_cost:
                    continue
                heapq.heappush(pq, (new_cost, new_node))
        else:
            for next_cost, new_node in adj_rev[node]:
                new_cost = cost + next_cost
                if dist[new_node] <= new_cost:
                    continue
                heapq.heappush(pq, (new_cost, new_node))
    return dist


n, m, x = map(int, input().split())
adj_for = [[] for _ in range(n+1)]
adj_rev = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj_for[a].append([c, b])
    adj_rev[b].append([c, a])


max_t = 0
dist_for, dist_rev = dijkstra(1), dijkstra(0)
for i in range(1, n+1):
    if max_t < dist_for[i] + dist_rev[i]:
        max_t = dist_for[i] + dist_rev[i]
print(max_t)
