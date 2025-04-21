import sys, heapq
input = sys.stdin.readline


def dijk(si, sj, ei, ej):
    pq = []
    heapq.heappush(pq, [0, si, sj])
    while pq:
        cost, i, j = heapq.heappop(pq)
        if i == ei and j == ej:
            return cost
        if dist[i][j] > cost:
            dist[i][j] = cost
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i + di, j + dj

                if 0 <= ni < r and 0 <= nj < c and dist[ni][nj] > cost + forest[ni][nj]:
                    heapq.heappush(pq, [cost + forest[ni][nj], ni, nj])


r, c = map(int, input().split())
forest = [[0] * c for _ in range(r)]
for i in range(r):
    info = input().rstrip()
    for j in range(c):
        if info[j] == 'g':
            forest[i][j] = 2500
        elif info[j] == 'S':
            start_i, start_j = i, j
        elif info[j] == 'F':
            end_i, end_j = i, j

for i in range(r):
    for j in range(c):
        if forest[i][j] == 2500:
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and forest[ni][nj] < 2:
                    forest[ni][nj] = 1

dist = [[float('inf')] * c for _ in range(r)]
result = dijk(start_i, start_j, end_i, end_j) - forest[end_i][end_j]

print(result//2500, result%2500)
