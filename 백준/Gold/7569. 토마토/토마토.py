import sys
input = sys.stdin.readline


def bfs(m, n, h):
    front = rear = -1
    for floor in range(h):
        for row in range(n):
            for column in range(m):
                if tomato[floor][row][column] == 1:
                    rear += 1
                    queue[rear] = floor, row, column

    last_day = 1
    while front != rear:
        front += 1
        f, r, c = queue[front]
        for df, dr, dc in delta:
            nf = f + df
            nr = r + dr
            nc = c + dc
            if 0 <= nf < h and 0 <= nr < n and 0 <= nc < m and tomato[nf][nr][nc] == 0:
                rear += 1
                queue[rear] = nf, nr, nc
                tomato[nf][nr][nc] = tomato[f][r][c] + 1
                if last_day < tomato[nf][nr][nc]:
                    last_day = tomato[nf][nr][nc]

    for floor in range(h):
        for row in range(n):
            for column in range(m):
                if tomato[floor][row][column] == 0:
                    return -1

    return last_day-1


M, N, H = map(int, input().split())
queue = [None] * M * N * H
delta = [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
tomato = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
print(bfs(M, N, H))
