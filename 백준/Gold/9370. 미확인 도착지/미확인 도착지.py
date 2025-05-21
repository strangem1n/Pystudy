import sys, heapq
input = sys.stdin.readline

def dijk(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist = [float('inf')] * (n+1)

    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        for next_cost, next_node in adj[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            heapq.heappush(pq, (cost+next_cost, next_node))
    result = []
    for node in x:
        if dist[node] % 2 == 1:
            result.append(node)
    result.sort()
    return result

t = int(input())
for tc in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        d *= 2
        if (a == g and b == h) or (a == h and b == g):
            d -= 1
        adj[a].append((d, b))
        adj[b].append((d, a))

    x = [int(input()) for _ in range(t)]
    ans = dijk(s)
    print(*ans)