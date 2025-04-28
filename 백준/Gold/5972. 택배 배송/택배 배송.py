import sys, heapq
input = sys.stdin.readline


def dijk():
    dist = [float('inf')] * (n+1)
    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue

        dist[node] = cost
        if node == n:
            return dist[node]

        for next_cost, next_node in adj[node]:
            new_cost = cost + next_cost
            if dist[next_node] <= new_cost:
                continue
            heapq.heappush(pq, [new_cost, next_node])


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

result = dijk()
print(result)
