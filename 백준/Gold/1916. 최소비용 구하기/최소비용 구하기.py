import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    start, *node = map(int, input().split())
    adj[start].append(node)  # 어떤 도시의 인접 도시와 버스 비용 저장

start_city, end_city = map(int, input().split())

cost = [float("inf")] * (N + 1)  # 각 도시까지의 최소 비용
cost[start_city] = 0

pq = [(0, start_city)]
while pq:
    sum_cost, city = heapq.heappop(pq)
    if cost[city] < sum_cost:    # 지금까지의 경로가 저장된 값보다 작으면 무시하고 가지치기
        continue

    for next_city, weight in adj[city]:  # 시작 도시부터 인접한 도시와 그 비용 꺼냄
        if cost[next_city] > sum_cost + weight:    # 최소 비용 갱신
            cost[next_city] = sum_cost + weight
            heapq.heappush(pq, (cost[next_city], next_city))

print(cost[end_city])