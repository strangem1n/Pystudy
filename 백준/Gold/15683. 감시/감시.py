import sys
input = sys.stdin.readline


def find_cctv():
    cctv = []
    for i in range(n):
        for j in range(m):
            if office[i][j] != 0 and office[i][j] != 6:
                cctv.append([i, j, office[i][j]])
    return cctv


def monitering(cnt, arr):
    global min_result
    if cnt == len(c):
        result = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    result += 1
        if min_result > result:
            min_result = result
    else:
        ci, cj, cctv_kind = c[cnt]
        for r in rotation[cctv_kind-1]:
            copy_arr = [a[:] for a in arr]
            for d in r:
                for k in range(1, 9):
                    ni = ci + delta_i[d]*k
                    nj = cj + delta_j[d]*k
                    if 0 <= ni < n and 0 <= nj < m:
                        if copy_arr[ni][nj] == 0:
                            copy_arr[ni][nj] = 7
                        elif copy_arr[ni][nj] == 6:
                            break
            monitering(cnt+1, copy_arr)


rotation = [[[0], [1], [2], [3]],
            [[0, 2], [1, 3]],
            [[0, 1], [1, 2], [2, 3], [3, 0]],
            [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            [[0, 1, 2, 3]]]

delta_i = [0, 1, 0, -1]
delta_j = [1, 0, -1, 0]

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
c = find_cctv()
min_result = n * m
monitering(0, office)
print(min_result)
