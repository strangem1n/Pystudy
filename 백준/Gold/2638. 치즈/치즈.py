from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def outer_air(r, c):
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and air_visited[nr][nc] == 0:
            air_visited[nr][nc] = 1
            if arr[nr][nc] == 1:
                continue
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
            outer_air(nr, nc)


def melt_cheese():
    visited = [[0] * m for _ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + dr[k], j + dc[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1:
                    visited[ni][nj] += 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] > 1:
                arr[i][j] = 2


def left_cheese():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return True
    return False


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
air_visited = [[0] * m for _ in range(n)]

day = 0
while left_cheese():
    day += 1
    outer_air(0, 0)
    air_visited = [[0] * m for _ in range(n)]
    melt_cheese()
print(day)
