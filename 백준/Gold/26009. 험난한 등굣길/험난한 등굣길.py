import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque([[0, 0]])
    while q:
        i, j = q.popleft()
        for ki in range(4):
            ni, nj = i + di[ki], j + dj[ki]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == arr[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if ni == n-1 and nj == m-1:
                    return visited[i][j]
                q.append([ni,nj])
    return -1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c, d = map(int, input().split())
    arr[r-1][c-1] = 1
    ri = r - 1
    ci = c - 1 + d

    for _ in range(d):
        if 0 <= ri < n and 0 <= ci < m:
            arr[ri][ci] = 1
        ci -= 1
        ri += 1

    for _ in range(d):
        if 0 <= ri < n and 0 <= ci < m:
            arr[ri][ci] = 1
        ci -= 1
        ri -= 1

    for _ in range(d):
        if 0 <= ri < n and 0 <= ci < m:
            arr[ri][ci] = 1
        ci += 1
        ri -= 1

    for _ in range(d):
        if 0 <= ri < n and 0 <= ci < m:
            arr[ri][ci] = 1
        ci += 1
        ri += 1

result = bfs()
if result == -1:
    print('NO')
else:
    print('YES')
    print(result)