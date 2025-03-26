from collections import deque


def infect(s, x, y):
    q = deque([])
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                q.append((arr[i][j], 0, i, j))
    q = deque(sorted(q))

    while q:
        virus, t, i, j = q.popleft()
        if t == s:
            break
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                arr[ni][nj] = virus
                q.append((virus, t+1, ni, nj))
    return arr[x-1][y-1]


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
print(infect(s, x, y))
