from collections import deque

def info(field):
    if field == '.':
        return 0
    elif field == 'S':
        return 1
    elif field == 'D':
        return 9
    elif field == '*':
        return 7
    elif field == 'X':
        return 8

def bfs(field):
    if field == 7:
        q = water_q
    elif field == 1:
        q = beaver_q
    length = len(q)
    for _ in range(length):
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if field == 7 and forest[ni][nj] < forest[i][j]:
                    forest[ni][nj] = 7
                    q.append([ni, nj])
                elif field == 1 and forest[ni][nj] in [0, 9] and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
forest = [None] * r
for i in range(r):
    forest[i] = list(map(info, input()))

water_q = deque([])
beaver_q = deque([])
visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if forest[i][j] == 1:
            beaver_q.append([i, j])
            visited[i][j] = 1
        elif forest[i][j] == 7:
            water_q.append([i, j])
        elif forest[i][j] == 9:
            ei, ej = i, j


while visited[ei][ej] == 0 and beaver_q:
    bfs(7)
    bfs(1)
if visited[ei][ej] != 0:
    print(visited[ei][ej]-1)
else:
    print('KAKTUS')
