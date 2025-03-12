def start(n):    # 가장 높은 봉우리 찾는 함수
    temp = []    # 좌표 기록할 리스트
    max_height = 0    # 초기값
    for i in range(n):
        for j in range(n):
            if max_height < arr[i][j]:    # 기존 최대 높이보다 크면 리스트까지 새롭게 갱신
                max_height = arr[i][j]
                temp = [[i, j]]
            elif max_height == arr[i][j]:    # 기존 최대 높이와 같으면 리스트에 추가
                temp.append([i, j])
    return temp


def dfs(r, c, length, cut):    # 가능한 만큼 쭉 가는 dfs 탐색
    global result
    current = arr[r][c]    # 현재 높이
    visited[r][c] = 1    # 방문 표시
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:    # 델타 탐색
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:    # 유효한 범위, 방문하지 않은 지점
            if arr[nr][nc] < current:    # 현재 위치보다 낮은 칸이면 갈 수 있음.
                dfs(nr, nc, length+1, cut)
            elif arr[nr][nc] - cut < current:    # 그렇지 않지만, 공사해서 갈 수 있는 칸이면
                save = arr[nr][nc]    
                arr[nr][nc] = current - 1    # 현재 칸보다 딱 1만 작아지는 게 최선.
                dfs(nr, nc, length+1, 0)    # 앞으로는 공사가 불가능하다!
                arr[nr][nc] = save    # 재귀가 끝나면 공사한 칸을 되돌려야 함.
    if result < length:
        result = length    # 가장 멀리 간 경로를 기록
    visited[r][c] = 0    # 재귀가 끝나면 방문 표시도 리셋


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    top = start(N)
    result = 0
    for i, j in top:
        dfs(i, j, 1, K)
    print(f"#{tc} {result}")
