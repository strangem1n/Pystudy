import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c, b):
    if r == c == 1:
        return 1

    q = deque([[0, 0, b]])
    for bi in range(b+1):
        visited[0][0][bi] = 1
    while q:
        i, j, left_b = q.popleft()
        for a in range(4):
            ni, nj = i + di[a], j + dj[a]
            if 0 <= ni < r and 0 <= nj < c:
                if arr[ni][nj] == 0:
                    if visited[ni][nj][left_b] == 0 or visited[ni][nj][left_b] > visited[i][j][left_b] + 1:
                        for left_bi in range(left_b+1):
                            visited[ni][nj][left_bi] = visited[i][j][left_b] + 1
                        if ni == r-1 and nj == c-1:
                            return visited[ni][nj][left_b]
                        q.append([ni, nj, left_b])
                elif arr[ni][nj] == 1 and left_b > 0:
                    if visited[ni][nj][left_b-1] == 0 or visited[ni][nj][left_b-1] > visited[i][j][left_b] + 1:
                        for left_bi in range(left_b):
                            visited[ni][nj][left_bi] = visited[i][j][left_b] + 1
                        q.append([ni, nj, left_b-1])
    return -1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n, m, k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
result = bfs(n, m, k)
print(result)