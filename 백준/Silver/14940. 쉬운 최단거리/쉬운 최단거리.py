def find(height, width):
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 2:
                return i, j


def bfs(r, c, height, width):
    front = rear = -1
    rear += 1
    queue[rear] = r, c
    while front != rear:
        front += 1
        here_r, here_c = queue[front]
        for dr, dc in delta:
            nr = here_r + dr
            nc = here_c + dc
            if 0 <= nr < height and 0 <= nc < width and arr[nr][nc] == 1:
                arr[nr][nc] = arr[here_r][here_c] + 1
                rear += 1
                queue[rear] = nr, nc

    for i in range(height):
        for j in range(width):
            if arr[i][j] > 1:
                arr[i][j] -= 2
            elif arr[i][j] == 1:
                arr[i][j] = -1
    pass


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = [None] * n * m
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
start_i, start_j = find(n, m)
bfs(start_i, start_j, n, m)
for row in range(n):
    print(*arr[row])
