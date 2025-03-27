from collections import deque


def bfs(n, ir, ic, fr, fc):
    if ir == fr and ic == fc:
        return 0

    visited = [[0] * n for _ in range(n)]
    q = deque([])
    q.append((ir, ic))
    visited[ir][ic] = 1

    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + move_r[i]
            nc = c + move_c[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                if nr == fr and nc == fc:
                    return visited[r][c]

                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))


move_r = [1, 2, 2, 1, -1, -2, -2, -1]
move_c = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(input())
for _ in range(T):
    length = int(input())
    init_r, init_c = map(int, input().split())
    final_r, final_c = map(int, input().split())
    print(bfs(length, init_r, init_c, final_r, final_c))
