import sys, heapq
input = sys.stdin.readline

def dijk(start):
    dist = [float('inf')] * (n+1)
    pq = []
    heapq.heappush(pq, [0, start])
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        for next_cost, next_node in adj[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            heapq.heappush(pq, [cost+next_cost, next_node])

    max_dist = 0
    cnt = 0
    for dis in dist:
        if dis != float('inf'):
            cnt += 1
            max_dist = max(max_dist, dis)
    return cnt, max_dist

t = int(input())
for tc in range(t):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append([s, a])
    print(*dijk(c))
