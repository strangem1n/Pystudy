import sys, heapq
input = sys.stdin.readline

def dijk(start, end):
    pq = []
    dist = [float('inf')] * (n+1)
    heapq.heappush(pq, [0, [start]])

    while pq:
        cost, citys = heapq.heappop(pq)
        if citys[-1] == end:
            return cost, citys

        if dist[citys[-1]] > cost:
            dist[citys[-1]] = cost

            for next_cost, next_city in adj[citys[-1]]:
                next_cost += cost
                if dist[next_city] > next_cost:
                    heapq.heappush(pq, [next_cost, citys+[next_city]])

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    adj[s].append([c, e])
s, e = map(int, input().split())
min_cost, min_city = dijk(s, e)
print(min_cost)
print(len(min_city))
print(*min_city)
