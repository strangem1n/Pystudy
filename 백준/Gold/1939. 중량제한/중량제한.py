import sys, heapq
input = sys.stdin.readline

def dijk(s, e):
    dist = [0] * (n+1)
    pq = []
    heapq.heappush(pq, (-float('inf'), s))
    while pq:
        cost, node = heapq.heappop(pq)
        cost = -cost
        if dist[node] >= cost:
            continue
        dist[node] = cost
        if node == e:
            return cost

        for next_cost, next_node in bridge[node]:
            max_cost = min(cost, next_cost)
            if dist[next_node] >= max_cost:
                continue
            heapq.heappush(pq, (-max_cost, next_node))

n, m = map(int, input().split())
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append((c, b))
    bridge[b].append((c, a))
fac1, fac2 = map(int, input().split())
result = dijk(fac1, fac2)
print(result)