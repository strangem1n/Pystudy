import sys
from collections import deque
from itertools import combinations


def bfs(i, j):
    q = deque([[i, j]])
    while q:
        i, j = q.popleft()
        board[i][j] = 0
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and board[ni][nj] == 1:
                q.append([ni, nj])

    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                return False
    return True


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
push = ''.join(sys.stdin.read().rstrip().split('\n'))
girl = list(map(lambda x: 1 if x == 'S' else 0, push))
test = [i for i in range(1, 26)]
result = combinations(test, 7)
cnt = 0
for r in result:
    if sum(map(lambda x: girl[x-1], r)) > 3:
        board = [[0] * 5 for _ in range(5)]
        for coord in r:
            coord -= 1
            board[coord//5][coord%5] = 1
        if bfs(coord//5, coord%5):
            cnt += 1
print(cnt)
