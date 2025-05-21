import sys, heapq
input = sys.stdin.readline
inf = 10 ** 7

def absolute_shortest(start, end):
    dist = [inf] * n
    use_edges = [set() for _ in range(n)]
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] < cost:
            continue

        for next_cost, next_node, edge_idx in adj[node]:
            if dist[next_node] < cost + next_cost:
                continue
            elif dist[next_node] == cost + next_cost:
                use_edges[next_node].update(use_edges[node])
                use_edges[next_node].add(edge_idx)
            else:
                dist[next_node] = cost + next_cost
                use_edges[next_node] = set(list(use_edges[node]))
                use_edges[next_node].add(edge_idx)
                heapq.heappush(pq, (cost+next_cost, next_node))
    return use_edges[end]

def near_shortest(start, end):
    dist = [inf] * n
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        if node == end:
            return cost
        for next_cost, next_node, edge_idx in adj[node]:
            if e_chk[edge_idx]:
                continue
            if dist[next_node] <= cost + next_cost:
                continue
            heapq.heappush(pq, (cost+next_cost, next_node))
    return -1


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    s, d = map(int, input().split())
    adj = [[] for _ in range(n)]
    e_chk = [False] * m
    for num in range(m):
        u, v, p = map(int, input().split())
        adj[u].append((p, v, num))
    for edge in absolute_shortest(s, d):
        e_chk[edge] = True
    print(near_shortest(s, d))
