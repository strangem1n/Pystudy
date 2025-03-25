import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
INF = 4e6
dij = [INF] * (V+1)

start = int(input())
dij[start] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

pq = [[0, start]]
while pq:
    cost, node = heapq.heappop(pq)
    if dij[node] < cost:
        continue

    for new_node, new_cost in adj[node]:
        if dij[new_node] < cost + new_cost:
            continue
        dij[new_node] = cost + new_cost
        heapq.heappush(pq, [cost+new_cost, new_node])

for i in range(1, V+1):
    if dij[i] == INF:
        print("INF")
    else:
        print(dij[i])
