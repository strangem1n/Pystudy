def dfs():
    stack = []
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == "#" and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = cnt
                stack.append((i, j))
                while stack:
                    r, c = stack.pop()
                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == "#" and visited[nr][nc] == 0:
                            visited[nr][nc] = cnt
                            stack.append((nr, nc))
    return cnt


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    arr = [input() for __ in range(H)]
    visited = [[0] * W for __ in range(H)]
    print(dfs())
