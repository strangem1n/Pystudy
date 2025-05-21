import sys
from copy import deepcopy
input = sys.stdin.readline

def move(shark_i, shark_j, shark_dir, shark_eat, array):
    global max_eat
    if max_eat < shark_eat:
        max_eat = shark_eat

    copy_a = deepcopy(array)

    for num in range(1, 17):
        switch = False
        for i in range(4):
            if switch:
                break
            for j in range(4):
                if switch:
                    break
                if copy_a[i][j][0] == num:
                    fish_dir = copy_a[i][j][1]
                    for k in range(8):
                        fish_d = (fish_dir + k) % 8
                        ni, nj = i + di[fish_d], j + dj[fish_d]
                        if 0 <= ni < 4 and 0 <= nj < 4 and copy_a[ni][nj][0] >= 0:
                            copy_a[i][j][1] = fish_d
                            copy_a[i][j][0], copy_a[ni][nj][0], copy_a[i][j][1], copy_a[ni][nj][1] = copy_a[ni][nj][0], copy_a[i][j][0], copy_a[ni][nj][1], copy_a[i][j][1]
                            switch = True
                            break

    next_shark_i = shark_i + di[shark_dir]
    next_shark_j = shark_j + dj[shark_dir]

    while 0 <= next_shark_i < 4 and 0 <= next_shark_j < 4:
        fish_value = copy_a[next_shark_i][next_shark_j][0]
        if fish_value > 0:
            copy_a[next_shark_i][next_shark_j][0] = -1
            copy_a[shark_i][shark_j][0] = 0
            move(next_shark_i, next_shark_j, copy_a[next_shark_i][next_shark_j][1], shark_eat+fish_value, copy_a)
            copy_a[next_shark_i][next_shark_j][0] = fish_value
            copy_a[shark_i][shark_j][0] = -1
        next_shark_i += di[shark_dir]
        next_shark_j += dj[shark_dir]

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

arr = []
for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    arr.append([[a1, b1-1], [a2, b2-1], [a3, b3-1], [a4, b4-1]])

shark_init = [0, 0]
eat, d = arr[0][0]
arr[0][0][0] = -1

max_eat = 0
move(0, 0, d, eat, arr)
print(max_eat)
