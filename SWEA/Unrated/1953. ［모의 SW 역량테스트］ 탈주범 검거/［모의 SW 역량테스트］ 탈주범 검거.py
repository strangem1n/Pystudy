# 터널 종류별 델타 탐색 방향
delta = [None, [[0,1], [1,0], [0,-1], [-1,0]], [[1,0], [-1,0]], [[0,1], [0,-1]],
         [[0,1], [-1,0]], [[0,1], [1, 0]], [[1,0], [0,-1]], [[-1,0], [0,-1]]]


def bfs(row, column, start_r, start_c, move):    # BFS 탐색
    visited = [[0] * column for _ in range(row)]
    queue_i = [0] * row * column
    queue_j = [0] * row * column
    front = rear = -1
    rear += 1
    queue_i[rear], queue_j[rear] = start_r, start_c
    visited[start_r][start_c] = 1    # 첫 맨홀 뚜껑 들어가는 데 걸린 시간 1
    result = 1    # 갈 수 있는 칸의 총 개수
    while front != rear:
        front += 1
        i, j = queue_i[front], queue_j[front]
        if arr[i][j] != 0:
            side = delta[arr[i][j]]    # 터널의 종류에 따라 di, dj 방향 리스트 가져옴
            for di, dj in side:
                ni = i + di
                nj = j + dj
                if 0 <= ni < row and 0 <= nj < column and arr[ni][nj] != 0 and visited[ni][nj] == 0:    # 범위 내이고 방문한 적 없으면
                    check = False    # 이 지점 터널의 출구와 인접한 지점 터널의 입구가 서로 이어져있는지 판단
                    if di == 0 and dj == 1 and arr[ni][nj] in [1, 3, 6, 7]:
                        check = True
                    elif di == 1 and dj == 0 and arr[ni][nj] in [1, 2, 4, 7]:
                        check = True
                    elif di == 0 and dj == -1 and arr[ni][nj] in [1, 3, 4, 5]:
                        check = True
                    elif di == -1 and dj == 0 and arr[ni][nj] in [1, 2, 5, 6]:
                        check = True

                    if check:    # 이어져있으면 큐에 다음 지점 넣기
                        rear += 1
                        queue_i[rear], queue_j[rear] = ni, nj
                        visited[ni][nj] = visited[i][j] + 1    # 이 칸까지 걸린 이동 시간은 전 칸의 visited 값 + 1
                        if visited[ni][nj] > move:    # 탈출 후 소요 시간보다 더 오래 걸리면 탐색 종료
                            return result
                        result += 1
    return result    # 더 이상 갈 수 있는 칸이 없어도 탐색 종료


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(N, M, R, C, L)
    print(f"#{tc} {result}")
