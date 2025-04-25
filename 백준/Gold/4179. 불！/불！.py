from collections import deque
import sys
input = sys.stdin.readline


def info(field):
    if field == '#':
        return 9
    elif field == '.':
        return 0
    elif field == 'J':
        return 1
    elif field == 'F':
        return 2

def bfs(field):
    if field == 1:
        q = jihoon
    elif field == 2:
        q = fire
    l = len(q)
    for _ in range(l):
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if field == 1 and maze[ni][nj] == visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    if ni == 0 or nj == 0 or ni == (r-1) or nj == (c-1):
                        return True
                    q.append([ni, nj])
                elif field == 2 and maze[ni][nj] < maze[i][j]:
                    maze[ni][nj] = 2
                    q.append([ni, nj])
    if field == 1:
        return False


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
maze = [None] * r
for i in range(r):
    maze[i] = list(map(info, input().rstrip()))

jihoon = deque([])
fire = deque([])
escaped = False
visited = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if maze[i][j] == 1:
            jihoon.append([i, j])
            visited[i][j] = 1
            if i == 0 or j == 0 or i == (r-1) or j == (c-1):
                escaped = True
        elif maze[i][j] == 2:
            fire.append([i, j])


cnt = 1
while not escaped and jihoon:
    cnt += 1
    bfs(2)
    escaped = bfs(1)
if escaped:
    print(cnt)
else:
    print('IMPOSSIBLE')
