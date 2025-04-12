import sys
input = sys.stdin.readline
from collections import deque

def find_gram():
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                return i, j


def bfs(si, sj, ei, ej, gram):
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1
    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                if ni == ei and nj == ej:
                    return visited[i][j]
                if maze[ni][nj] != 1 or gram:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    return 10001

n, m, b = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
g1, g2 = find_gram()

res_1 = bfs(0, 0, n-1, m-1, False)
res_2 = bfs(0, 0, g1, g2, False) + bfs(g1, g2, n-1, m-1, True)
result = min(res_1, res_2)
if result > b:
    print('Fail')
else:
    print(result)
