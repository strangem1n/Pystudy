def dfs(queen, limit):
    global result
    if queen == limit:    # 퀸을 다 놓으면 경우의 수 하나 세기
        result += 1

    else:
        for i in range(limit):    # 퀸은 무조건 가로줄 하나에 하나씩만 들어간다.
            if used_column[i] == 0 and cross_plus[i+queen] == 0 and cross_minus[limit-1+i-queen] == 0:
                used_column[i] = 1
                cross_plus[queen+i] = 1
                cross_minus[limit-1+i-queen] = 1
                dfs(queen+1, limit)
                used_column[i] = 0
                cross_plus[queen+i] = 0
                cross_minus[limit-1+i-queen] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    used_column = [0] * n    # 같은 세로줄에 퀸이 있는지 판단
    cross_plus = [0] * (2 * (n-1) + 1)    # 오른쪽 위 대각선 방향에 퀸이 있는지 판단 (좌표의 x+y 값이 같으면 같은 대각선상)
    cross_minus = [0] * (2 * (n-1) + 1)    # 오른쪽 아래 대각선 방향에 퀸이 있는지 판단 (좌표의 x-y 값이 같으면 같은 대각선상)
    result = 0
    dfs(0, n)
    print(f"#{tc} {result}")
