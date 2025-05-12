import sys
from collections import deque
input = sys.stdin.readline

def snake():
    q = deque([[0, 0]])
    t = 0
    side = 0
    change_idx = 0
    while q:
        i, j = q[-1]
        t += 1
        ni, nj = i+di[side], j+dj[side]

        if -1 == ni or -1 == nj or board == ni or board == nj:
            return t

        for self_i, self_j in q:
            if self_i == ni and self_j == nj:
                return t

        if change_idx < order and t == orders[change_idx][0]:
            side = (side + orders[change_idx][1] + 4) % 4
            change_idx += 1

        for k in range(apple):
            if apple_ate[k] == 0:
                ai, aj = apples[k]
                if ni == ai and nj == aj:
                    q.append([ni, nj])
                    apple_ate[k] = 1
                    break
        else:
            q.append([ni, nj])
            q.popleft()
    return t

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

board = int(input())
apple = int(input())
apples = [list(map(lambda x: int(x)-1, input().split())) for _ in range(apple)]
apple_ate = [0] * apple
order = int(input())
orders = [list(map(lambda x: 1 if x == 'D' else -1 if x == 'L' else int(x), input().split())) for _ in range(order)]
print(snake())
