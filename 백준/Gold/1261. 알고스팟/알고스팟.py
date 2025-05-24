import sys, heapq
input = sys.stdin.readline

def dijk():
    dist = [[m*n] * m for _ in range(n)]
    pq = []
    heapq.heappush(pq, ((0, 0, 0)))

    while pq:
        cost, i, j = heapq.heappop(pq)
        if dist[i][j] <= cost:
            continue
        dist[i][j] = cost
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if maze[ni][nj] == 1 and dist[ni][nj] > cost + 1:
                    heapq.heappush(pq, (cost+1, ni, nj))
                elif maze[ni][nj] == 0 and dist[ni][nj] > cost:
                    heapq.heappush(pq, (cost, ni, nj))
    
    return dist[n-1][m-1]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

m, n = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
print(dijk())