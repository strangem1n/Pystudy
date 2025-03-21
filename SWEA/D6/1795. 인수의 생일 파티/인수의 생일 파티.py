import heapq


def dijkstra(start, end, vertex):
    cost = [float("inf")] * (vertex + 1)
    cost[start] = 0
    pq = [(0, start)]
    while pq:
        current_cost, current_v = heapq.heappop(pq)
        if cost[current_v] < current_cost:    # 현재까지 거리가 저장된 값보다 크면 무시
            continue

        for next_v, weight in adj[current_v]:
            next_cost = current_cost + weight
            if cost[next_v] > next_cost:    # 저장된 값보다 최단거리이면 갱신하기
                cost[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))
    return cost[end]    # 시작지점에서 도착지점까지의 최단경로 거리


T = int(input())
for tc in range(1, T+1):
    v, node, end_house = map(int, input().split())
    adj = [[] for _ in range(v+1)]    # 각 정점에 인접한 정점과 노드 가중치 저장
    for _ in range(node):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    max_time = 0
    for start_house in range(1, v+1):    # 어떤 지점에서 X까지 최단경로 + X에서 어떤 지점까지 최단경로 합을 1부터 N까지 전부 검사
        total_time = dijkstra(start_house, end_house, v) + dijkstra(end_house, start_house, v)
        if max_time < total_time:    # 최댓값 갱신
            max_time = total_time
    print(f"#{tc} {max_time}")
