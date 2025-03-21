import heapq


def dijkstra(end):
    visited = [[float("inf")] * end for _ in range(end)]
    visited[0][0] = 0
    pq = [(0, 0, 0)]
    while pq:
        cost, i, j = heapq.heappop(pq)
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < end and 0 <= nj < end:
                new_cost = cost + arr[ni][nj]
                if visited[ni][nj] > new_cost:
                    visited[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    return visited[end-1][end-1]


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = dijkstra(N)
    print(f"#{tc} {result}")
