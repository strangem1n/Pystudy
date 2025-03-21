import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    q = [(0, 0)]
    used = [0] * N
    min_cost = 0

    dists = [2e12] * N
    dists[0] = 0

    while q:
        cost, node = heapq.heappop(q)

        if used[node]:
            continue

        used[node] = 1
        min_cost += cost

        for next_node in range(N):
            if used[next_node]:
                continue

            next_cost = (island_x[next_node] - island_x[node]) ** 2 + (island_y[next_node] - island_y[node]) ** 2
            if next_cost < dists[next_node]:
                dists[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
                
    print(f"#{tc} {round(min_cost*E)}")
