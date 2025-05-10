import sys, heapq
input = sys.stdin.readline

def dijk(start):
    pq = []
    dist = [float('inf')] * (n+1)
    route = [0] * (n+1)
    heapq.heappush(pq, [0, start, '-'])
    while pq:
        cost, node, r = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        dist[node] = cost
        route[node] = r
        for next_cost, next_node in adj[node]:
            if cost + next_cost > dist[next_node]:
                continue
            if r == '-':
                heapq.heappush(pq, [cost+next_cost, next_node, next_node])
            else:
                heapq.heappush(pq, [cost+next_cost, next_node, r])

    return route[1:]

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

for i in range(1, n+1):
    print(*dijk(i))
