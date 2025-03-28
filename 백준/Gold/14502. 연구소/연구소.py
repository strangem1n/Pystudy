from collections import deque


def init_safe():    # 초기 안전영역
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


def find_virus():    # 초기 바이러스 위치
    virus = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virus.append((i, j))
    return virus


def make_wall(cnt, r, c):    # 재귀를 통한 벽 세우기
    if cnt == 3:
        copy_arr = [a[:] for a in arr]    # 벽을 세운 연구소 배열 복사
        copy_q = deque([xy for xy in queue])    # 초기 바이러스 위치 복사
        bfs(copy_arr, copy_q)
    else:    # 벽을 세울 3개의 위치를 뽑을 때 중복을 없애기 위해 이전에 세웠던 벽의 위치 다음 칸부터 순회함
        for i in range(r, n):
            if i == r:    # 2차원 배열의 순회는 각 행을 하나 뽑아서 열을 순회하므로, 이전 좌표 (r, c)라면 (r, c+1)부터 시작.
                for j in range(c+1, m):
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                        make_wall(cnt+1, i, j)
                        arr[i][j] = 0
            else:    # r+1부터는 상관없다.
                for j in range(m):
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                        make_wall(cnt+1, i, j)
                        arr[i][j] = 0


def bfs(array, q):    # 벽을 세운 연구소에서 초기 바이러스 좌표로부터 bfs 돌려서 감염 확인
    global max_safe
    infected = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                array[nx][ny] = 2
                infected += 1    # 감염된 공간의 수
                q.append((nx, ny))
    safe = initial - (infected+3)    # 안전 영역 = 초기 안전에서 (감염된 공간 + 3개의 벽)을 뺀 수.
    if max_safe < safe:
        max_safe = safe    # 최댓값 갱신


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
initial = init_safe()
max_safe = 0
queue = find_virus()
make_wall(0, 0, -1)    # 맨 처음 벽을 세운 위치를 (0, -1)이라고 두어 재귀함수가 (0, 0)부터 순회하도록 함
print(max_safe)
