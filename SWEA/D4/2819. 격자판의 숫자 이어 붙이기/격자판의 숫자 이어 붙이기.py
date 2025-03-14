def dfs(r, c, num, num_len):    # DFS 탐색, 6번 이동한 경로를 통해 수를 만들기
    global result
    if num_len == 7:    # 숫자의 길이가 7이 되면
        if num not in memo:    # 이미 만들어진 수가 아니면 기록하기
            result += 1
            memo.append(num)
    else:
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:    # 델타 탐색
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:    # 유효범위 설정, 한 번 간 곳을 다시 갈 수 있으므로 visited 배열은 필요 없음
                dfs(nr, nc, num + arr[nr][nc], num_len + 1)    # 다음 지점으로 가서 반복


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    memo = []
    result = 0
    for i in range(4):    # 임의의 점에서 시작
        for j in range(4):
            dfs(i, j, arr[i][j], 1)
    print(f"#{tc} {result}")
