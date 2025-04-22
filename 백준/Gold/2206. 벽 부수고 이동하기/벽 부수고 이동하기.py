import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]
visited[0][0] = [1, 1]
q = deque([[0, 0, 1]])
while q:
    i, j, b = q.popleft()
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 0:
                if b == 1 and visited[ni][nj][0] == 0:
                    visited[ni][nj][0] = visited[i][j][0] + 1
                    q.append([ni, nj, b])
                elif b == 0 == visited[ni][nj][1]:
                    visited[ni][nj][1] = visited[i][j][1] + 1
                    q.append([ni, nj, b])
            elif arr[ni][nj] == 1 == b:
                visited[ni][nj][1] = visited[i][j][0] + 1
                q.append([ni, nj, 0])

result = visited[n-1][m-1]
if result[0] == result[1] == 0:
    print(-1)
else:
    if result[0] == 0:
        print(result[1])
    elif result[1] == 0:
        print(result[0])
    else:
        print(min(result))
