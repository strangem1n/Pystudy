import sys
from collections import deque
input = sys.stdin.readline

def bfs(ri, ci):
    q = deque([[ri, ci]])
    wall = set()
    cnt = 1
    visited[ri][ci] = cnt
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == visited[ni][nj] == 0:
                    cnt += 1
                    visited[ni][nj] = cnt
                    q.append([ni, nj])
                elif arr[ni][nj] == 1:
                    wall.add((ni, nj))
    for wi, wj in wall:
        result[wi][wj] = (result[wi][wj] + cnt) % 10

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            result[r][c] = (result[r][c] + 1) % 10
        elif visited[r][c] == 0:
            bfs(r, c)

for r in range(n):
    for c in range(m):
        print(result[r][c], end="")
    print("")