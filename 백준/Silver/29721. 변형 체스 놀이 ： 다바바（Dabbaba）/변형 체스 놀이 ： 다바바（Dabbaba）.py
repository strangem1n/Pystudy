import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = {}
q = [[0, 0] for _ in range(k)]

for i in range(k):
    r, c = map(int, input().split())
    visited[(r-1)*n+(c-1)] = 1
    q[i][0], q[i][1] = r-1, c-1

dr = [2, 0, -2, 0]
dc = [0, 2, 0, -2]

cnt = 0
for i in range(k):
    r, c = q[i]
    for j in range(4):
        nr, nc = r+dr[j], c+dc[j]
        if 0 <= nr < n and 0 <= nc < n:
            if visited.get(nr*n+nc):
                continue
            else:
                visited[nr*n+nc] = 1
                cnt += 1
print(cnt)
