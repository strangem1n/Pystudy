import sys
from collections import deque
input = sys.stdin.readline

def fill(field):
    if field == 'S':
        return 1
    elif field == '.':
        return 0
    elif field == '#':
        return 9
    elif field == 'E':
        return 2

def find_start(field):
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if field == building[i][j][k]:
                    return i, j, k

def bfs(x, y, z):
    q = deque([[x, y, z]])
    visited[x][y][z] = 1
    while q:
        i, j, k = q.popleft()
        for m in range(6):
            ni, nj, nk = i+di[m], j+dj[m], k+dk[m]
            if 0 <= ni < l and 0 <= nj < r and 0 <= nk < c and visited[ni][nj][nk] == 0 and building[ni][nj][nk] != 9:
                visited[ni][nj][nk] = visited[i][j][k] + 1
                if ni == el and nj == er and nk == ec:
                    return visited[ni][nj][nk]-1
                q.append([ni, nj, nk])
    return -1

di = [0, 0, 0, 0, 1, -1]
dj = [1, 0, -1, 0, 0, 0]
dk = [0, 1, 0, -1, 0, 0]

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break
    building = [None] * l
    for i in range(l):
        building[i] = [list(map(fill, input().rstrip())) for _ in range(r)]
        input()

    sl, sr, sc = find_start(1)
    el, er, ec = find_start(2)

    visited = [[[0] * c for _ in range(r)] for __ in range(l)]
    result = bfs(sl, sr, sc)
    if result == -1:
        print('Trapped!')
    else:
        print(f"Escaped in {result} minute(s).")
