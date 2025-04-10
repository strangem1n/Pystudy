import sys
input = sys.stdin.readline
from collections import deque


def init():
    q = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] != 0:
                visited[i][j] = 1
                q.append((i, j, arr[i][j]))
    if not q:
        q = [(0, 0, 0)]
    return q


def chunk(ii, ij):
    copy_arr = [a[:] for a in visited]
    q = deque([(ii, ij)])
    while q:
        i, j = q.popleft()
        copy_arr[i][j] = 0
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and copy_arr[ni][nj] == 1:
                copy_arr[ni][nj] = 0
                q.append((ni, nj))

    for i in range(m):
        for j in range(n):
            if copy_arr[i][j] == 1:
                return False
    return True


def add(array):
    new_q = deque([])
    while array:
        i, j, length = array.popleft()
        i -= length
        j -= length
        for di in range(2*length+1):
            for dj in range(2*length+1):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if visited[ni][nj] == 0 or arr[ni][nj] < length:
                        arr[ni][nj] = length
                        visited[ni][nj] = 1
                        new_q.append((ni, nj, length))
    return new_q


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

init_q = init()
init_i, init_j, _ = init_q[0]
next_q = deque(init_q)
day = 0
while True:
    chk = chunk(init_i, init_j)
    if chk:
        break
    else:
        next_q = add(next_q)
        day += 1
print(day)
