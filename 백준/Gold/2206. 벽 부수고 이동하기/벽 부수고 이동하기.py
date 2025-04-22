import sys
from collections import deque
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs():
    if n == m == 1:
        return 1

    q = deque([[0, 0, 1]])
    while q:
        i, j, b = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0:
                    if ni == n-1 and nj == m-1:
                        result = visited[i][j][0] + 1 if b == 1 else visited[i][j][1] + 1
                        return result
                    elif b == 1 and visited[ni][nj][0] == 0:
                        visited[ni][nj][0] = visited[i][j][0] + 1
                        q.append([ni, nj, b])
                    elif b == 0 == visited[ni][nj][1]:
                        visited[ni][nj][1] = visited[i][j][1] + 1
                        q.append([ni, nj, b])
                elif arr[ni][nj] == 1 == b:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    q.append([ni, nj, 0])
    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]
visited[0][0] = [1, 1]
print(bfs())