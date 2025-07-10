import sys, heapq
input = sys.stdin.readline

def solve():
    pq = []
    dist = [[float('inf')] * n for _ in range(n)]
    heapq.heappush(pq, [0, 0, 0])
    while pq:
        cost, i, j = heapq.heappop(pq)
        if dist[i][j] <= cost:
            continue
        dist[i][j] = cost
        if i == j == (n-1):
            return cost
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '0':
                    if dist[ni][nj] <= cost + 1:
                        continue
                    heapq.heappush(pq, [cost+1, ni, nj])
                else:
                    if dist[ni][nj] <= cost:
                        continue
                    heapq.heappush(pq, [cost, ni, nj])
    return dist[n-1][n-1]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n = int(input())
maze = [input().rstrip() for _ in range(n)]
print(solve())