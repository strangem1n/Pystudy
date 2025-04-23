import sys, collections
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def melt_ice():
    new_ice = []
    for r in range(n):
        for c in range(m):
            if ocean[r][c] > 0:
                cnt = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and ocean[nr][nc] == 0:
                        cnt += 1
                if ocean[r][c] - cnt <= 0:
                    new_ice.append([r, c])
                else:
                    ocean[r][c] -= cnt
    for r, c in new_ice:
        ocean[r][c] = 0


def find_ice(arr):
    for r in range(n):
        for c in range(m):
            if arr[r][c] > 0:
                return r, c
    return False


def is_separated(r, c):
    copy_ocean = [o[:] for o in ocean]
    q = collections.deque([])
    q.append([r, c])
    copy_ocean[r][c] = 0
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0 <= nr < n and 0 <= nc < m and copy_ocean[nr][nc] > 0:
                copy_ocean[nr][nc] = 0
                q.append([nr, nc])

    if find_ice(copy_ocean):
        return True
    else:
        return False


n, m = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(n)]
water = []
for i in range(n):
    for j in range(m):
        if ocean[i][j] == 0:
            water.append([i, j])

year = 0
all_melt = True
while find_ice(ocean):
    i, j = find_ice(ocean)
    if is_separated(i, j):
        all_melt = False
        break
    year += 1
    melt_ice()


if all_melt:
    print(0)
else:
    print(year)
