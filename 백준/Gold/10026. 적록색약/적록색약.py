def dfs(n, status):
    visited = [[0] * n for _ in range(n)]
    area = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                area += 1
                visited[i][j] = area
                top = 0
                stack[top] = (i, j)
                while top > -1:
                    r, c = stack[top]
                    for dr, dc in delta:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                            if arr[r][c] == arr[nr][nc] or (status == "weak" and arr[r][c] in color and arr[nr][nc] in color):
                                visited[nr][nc] = area
                                top += 1
                                stack[top] = (nr, nc)
                                break
                    else:
                        top -= 1
    return area


stack = [None] * 10000
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
color = ["R", "G"]

n = int(input())
arr = [input() for _ in range(n)]

print(dfs(n, "normal"), dfs(n, "weak"))
