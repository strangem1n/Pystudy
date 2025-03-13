def bfs(explosion, block_cnt, arr):
    global result
    if explosion == 0:    # 남은 구슬 발사 횟수가 0이면 전달받은 남은 벽돌 수와 비교
        if result > block_cnt:
            result = block_cnt

    elif block_cnt == 0:    # 구슬 발사 횟수가 남아있지만 남은 벽돌이 0이면 바로 종료
        result = 0
        return

    else:
        for c in range(W):    # 왼쪽에서 오른쪽으로 순회하면서 가능한 경우 모두 보기
            remove_block = 0    # 이번에 제거한 벽돌의 개수
            r = 0
            while r < H and arr[r][c] == 0:    # 위에서부터 아래로 순회하면서 부술 벽돌이 있는지 확인
                r += 1

            if r == H:    # 부술 벽돌이 없으면 바로 오른쪽으로 이동
                continue

            temp = [arr[x][:] for x in range(H)]    # 원본 벽돌 배열을 지키기 위해 복사하기
            front = rear = -1    # BFS를 이용해 부술 수 있는 벽돌과 폭발 범위를 큐에 넣기
            rear += 1
            queue_r[rear], queue_c[rear], queue_ex[rear] = r, c, temp[r][c]
            temp[r][c] = 0
            while front != rear:    # 큐에서 하나씩 꺼내기
                front += 1
                remove_block += 1    # 큐에서 꺼낼 때마다 부서진 벽돌 개수 하나씩 추가함
                for k in range(queue_ex[front]):    # 폭발 범위만큼 델타 탐색
                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nr = queue_r[front] + dr * k
                        nc = queue_c[front] + dc * k
                        if 0 <= nr < H and 0 <= nc < W and temp[nr][nc] != 0:    # 유효한 범위이고, 벽돌이 있으면 큐에 넣기
                            rear += 1
                            queue_r[rear], queue_c[rear], queue_ex[rear] = nr, nc, temp[nr][nc]
                            temp[nr][nc] = 0    # 배열 상에서 미리 벽돌을 없애서 중복해서 큐에 넣는 것 방지

            for x in range(W):    # 벽돌이 다 부서진 후 처리
                for y in range(H-1, 0, -1):
                    if temp[y][x] == 0:    # 빈 공간을 발견하면
                        idx = y - 1
                        while idx > -1 and temp[idx][x] == 0:    # 빈 공간 위에 벽돌 있는지 탐색
                            idx -= 1
                        if idx == -1:    # 없으면 다음(오른쪽) 줄로 넘어가기
                            continue
                        else:    # 있으면 빈 공간과 벽돌을 맞바꿈
                            temp[y][x], temp[idx][x] = temp[idx][x], temp[y][x]

            bfs(explosion-1, block_cnt - remove_block, temp)    # 발사 횟수 1회 줄어들고, 남은 벽돌 수와 폭발 결과를 전달


T = int(input())

queue_r = [0] * 12 * 15
queue_c = [0] * 12 * 15
queue_ex = [0] * 12 * 15

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(H)]
    block = 0
    for i in range(H):
        for j in range(W):
            if array[i][j] != 0:    # 첫 벽돌 개수를 세기
                block += 1
    result = block
    bfs(N, block, array)
    print(f"#{tc} {result}")
