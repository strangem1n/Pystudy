import sys
from collections import deque
input = sys.stdin.readline

def differ(si, sj, kind):
    q = deque([[si, sj]])
    used[si][sj] = 1
    while q:
        i, j = q.popleft()
        arr[i][j] = kind
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and used[ni][nj] == 0:
                used[ni][nj] = 1
                q.append([ni, nj])

def bfs(si, sj):
    global min_bridge
    q = deque([[si, sj]])
    visited = [[0] * n for _ in range(n)]
    visited[si][sj] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if visited[ni][nj] >= min_bridge + 1 or (arr[ni][nj] > 0 and arr[ni][nj] != arr[si][sj]):
                    return visited[ni][nj]-1
                elif arr[ni][nj] == 0:
                    q.append([ni, nj])
    return n ** 2

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
used = [[0] * n for _ in range(n)]

cnt = 1
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            cnt += 1
            differ(r, c, cnt)


min_bridge = n ** 2
for r in range(n):
    for c in range(n):
        if arr[r][c] > 1:
            for idx in range(4):
                nr, nc = r+di[idx], c+dj[idx]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
                    min_bridge = min(min_bridge, bfs(r, c))
                    break
print(min_bridge-1)