from collections import deque


def bfs(y, x):
    q = deque([])
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1:
                q.append((i, j))

    safe = 0

    while q:
        r, c = q.popleft()
        for dr, dc in [[1, 0], [0, 1], [1, 1], [1, -1], [-1, 0], [-1, -1], [-1, 1], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < y and 0 <= nc < x and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
                if safe < arr[nr][nc]:
                    safe = arr[nr][nc]

    return safe - 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs(n, m))