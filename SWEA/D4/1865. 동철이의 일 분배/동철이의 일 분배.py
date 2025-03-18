def solve(num, p, limit):
    global max_p
    if p <= max_p:    # 현재 확률이 저장된 최댓값보다 작아지면 가지치기
        return

    if num == limit:    # 모든 성공확률 다 곱해서 최댓값과 비교
        if max_p < p:
            max_p = p
    else:
        for i in range(limit):    # 각 사람 뽑아서 성공확률 곱하기
            if used[i] == 0:
                used[i] = 1
                solve(num+1, p*arr[i][num], limit)
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]    # 입력받은 백분율 값을 소수로 변환
    max_p = 0
    used = [0] * N
    solve(0, 1, N)
    print(f"#{tc} {max_p*100:.6f}")    # 소수점 6번째까지 출력
