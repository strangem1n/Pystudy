import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    q = deque([(si, sj)])
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n and 0 <= nj < m and treasure[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    return visited[i][j]-1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
n, m = map(int, input().split())
treasure = [list(map(lambda x: 0 if x == 'L' else 1, input().rstrip())) for _ in range(n)]

max_dist = 0
for r in range(n):
    for c in range(m):
        if treasure[r][c] == 0:
            max_dist = max(max_dist, bfs(r, c))
print(max_dist)
