from collections import deque


def find_cleaner():    # 공기청정기 좌표 찾기
    for i in range(r):
        if arr[i][0] == -1:
            return [i, i+1]


def find_dust():    # 초기 전체 먼지의 양
    d = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                d += arr[i][j]
    return d


def diffusion():    # 1. 먼지 확산
    q = deque([])
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:    # 먼지가 있는 곳의 좌표, 먼지의 양 저장
                q.append((i, j, arr[i][j]))

    while q:
        i, j, dust = q.popleft()
        diff_dust = dust // 5    # 확산된다면 퍼질 먼지의 양
        cnt = 0    # 확산 횟수
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] > -1:
                cnt += 1
                arr[ni][nj] += diff_dust    # 확산된 곳에 먼지 추가
        arr[i][j] -= diff_dust * cnt    # 확산된 만큼 기존 먼지 칸에서 제거


def clean():    # 2. 공기청정기로 인한 순환
    remove = 0    # 이번 순환으로 제거된 먼지의 양

    cleaner_top, cleaner_down = cleaner    # 위쪽은 반시계, 오른쪽은 시계로 회전한다.
    i = cleaner_top - 1
    j = 0
    remove += arr[i][j]    # 공기청정기 바로 위 좌표에 있던 먼지는 사라짐. 회전을 거꾸로 짚으면서 사라진 빈 칸을 그 전 칸이 채워준다.

    while i > 0:    # ↓
        arr[i][j] = arr[i-1][j]
        i -= 1
    while j < c-1:    # ←
        arr[i][j] = arr[i][j+1]
        j += 1
    while i < cleaner_top:    # ↑
        arr[i][j] = arr[i+1][j]
        i += 1
    while j > 1:    # →
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = 0    # 공기청정기에서 나온 바람은 먼지가 없다.

    i = cleaner_down + 1
    j = 0
    remove += arr[i][j]    # 공기청정기 바로 아래 좌표 먼지를 제거

    while i < r-1:    # ↑
        arr[i][j] = arr[i+1][j]
        i += 1
    while j < c-1:    # ←
        arr[i][j] = arr[i][j+1]
        j += 1
    while i > cleaner_down:    # ↓
        arr[i][j] = arr[i-1][j]
        i -= 1
    while j > 1:    # →
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = 0    # 공기청정기에서 나온 바람

    return remove


r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cleaner = find_cleaner()
total_dust = find_dust()
for _ in range(t):
    diffusion()
    total_dust -= clean()    # 전체 먼지에서 이번에 사라진 먼지의 양을 뺀다.
print(total_dust)    # 남아있는 먼지의 양
