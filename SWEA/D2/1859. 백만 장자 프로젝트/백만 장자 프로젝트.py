T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 배열에 거꾸로 접근해서 현재 날보다 전날에 더 싸면 이득을 (현재 가격) - (전날 가격) 만큼 얻을 수 있다.
    result = 0    # 전체 이익
    benefit = 0    # 현재 이익
    current = arr[-1]    # 현재 가격
    for i in range(N-2, -1, -1):
        chk = arr[i]    # 전날 가격
        if current < chk:    # 전날 더 비싸면
            result += benefit    # 그동안의 이익 전체에 합치고 초기화
            benefit = 0
            current = chk    # 전날 가격이 새로운 기준이 됨
        elif current > chk:    # 전날 더 싸면
            benefit += current - chk    # 이익을 추가하고 계속 순회

    if benefit > 0:    # 마지막에 더하지 못한 현재 이익까지 더해주기
        result += benefit

    print(f"#{tc} {result}")
    