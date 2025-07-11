import sys, heapq
input = sys.stdin.readline
INF = 1000*1000

def dijkstra(start, end):
    dist = [[INF] * n for _ in range(n+1)]
    pq = []
    heapq.heappush(pq, [0, start, 0])
    dist[start][0] = 0

    while pq:
        cost, node, v = heapq.heappop(pq)
        is_true = True
        for v0 in range(v+1):
            if dist[node][v0] < cost:
                is_true = False
                break

        if is_true:
            for next_cost, next_node in adj[node]:
                if v < n-1 and dist[next_node][v+1] > cost + next_cost:
                    dist[next_node][v+1] = cost + next_cost
                    heapq.heappush(pq, [cost + next_cost, next_node, v+1])
    return dist[end]

n, m, k = map(int, input().split())
s, d = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append([w, b])
    adj[b].append([w, a])
increase = [int(input()) for _ in range(k)]
for i in range(1, k):
    increase[i] += increase[i-1]

result = dijkstra(s, d)

init_ans = INF
limit = n
for i in range(n):
    if init_ans > result[i]:
        init_ans = result[i]
        limit = i
print(init_ans)

for i in range(k):
    add = increase[i]
    min_ans = INF
    for j in range(limit+1):
        if result[j] == INF:
            continue
        ans = result[j] + (add * j)
        if min_ans > ans:
            min_ans = ans
            limit = j
    print(min_ans)
