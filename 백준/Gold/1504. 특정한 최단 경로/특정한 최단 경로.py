import sys
import heapq
input = sys.stdin.readline


def dijkstra(init, last):
    pq = [[0, init]]
    dis = [float('inf')] * (n+1)
    dis[init] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if dis[node] < cost:
            continue
        dis[node] = cost
        if node == last:
            return cost
        for new_cost, new_node in adj[node]:
            next_cost = dis[node] + new_cost
            if dis[new_node] > next_cost:
                heapq.heappush(pq, [next_cost, new_node])


n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(e):
    start, end, dist = map(int, input().split())
    adj[start].append([dist, end])
    adj[end].append([dist, start])
v1, v2 = map(int, input().split())

try:
    dis1 = dijkstra(1, v1)
    dis2 = dijkstra(1, v2)
    dis3 = dijkstra(v1, v2)
    dis4 = dijkstra(v1, n)
    dis5 = dijkstra(v2, n)

    if dis1 + dis5 < dis2 + dis4:
        print(dis1+dis3+dis5)
    else:
        print(dis2+dis3+dis4)
except:
    print(-1)