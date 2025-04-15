import sys,heapq
input = sys.stdin.readline


def dijkstra(N):
    pq = []
    heapq.heappush(pq, (arr[0][0], 0, 0))
    while pq:
        cost, i, j = heapq.heappop(pq)
        if dist[i][j] <= cost:
            continue
        dist[i][j] = cost
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni == nj == N-1:
                return cost + arr[ni][nj]
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = cost + arr[ni][nj]
                if dist[ni][nj] <= new_cost:
                    continue
                heapq.heappush(pq, (new_cost, ni, nj))


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
cnt = 0

while True:
    n = int(input())
    if n == 0:
        break
    cnt += 1

    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]
    result = dijkstra(n)
    print(f'Problem {cnt}: {result}')
