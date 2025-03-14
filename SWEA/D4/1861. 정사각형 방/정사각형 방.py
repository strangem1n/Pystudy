def move(r, c):
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:    # 델타 탐색
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] - 1) == arr[r][c]:    # 범위 내에서 현재 칸보다 1 높은 칸 발견하면
            return 1 + move(nr, nc)    # 1칸 진행
            break
    else:
        return 0    # 더 이상 진행하지 못하면 종료


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    move_cnt = [1] * (N ** 2 + 1)    # 각 칸에서 최대 얼마만큼 이동 가능한지 저장할 리스트

    for i in range(N):
        for j in range(N):
            move_cnt[arr[i][j]] += move(i, j)    # 각 칸에 이동 가능한 칸의 수를 더해줌

    max_move = 0
    max_idx = 0
    for i in range(1, N ** 2 + 1):
        if max_move < move_cnt[i]:    # 이동 가능한 거리 최댓값이 여러개이면 수가 더 적은 것을 선택
            max_move = move_cnt[i]
            max_idx = i

    print(f"#{tc} {max_idx} {max_move}")
