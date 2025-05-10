import sys, heapq
input = sys.stdin.readline

def dijk():
    dist = [float('inf')] * (n+1)
    used_v = [[] for _ in range(n+1)]
    pq = []
    heapq.heappush(pq, [0, 1, []])
    while pq:
        cost, node, v_list = heapq.heappop(pq)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        used_v[node] = v_list
        for next_cost, next_node in adj[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            heapq.heappush(pq, [cost+next_cost, next_node, v_list+[[node, next_node]]])
    return used_v


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

v = []
used = dijk()
cnt = 0
for u in used:
    for a, b in u:
        if [a, b] not in v and [b, a] not in v:
            v.append([a, b])
            cnt += 1
print(cnt)
for a, b in v:
    print(a, b)
