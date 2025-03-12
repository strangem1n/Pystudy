def f(initial, idx, limit):    # 연산자의 남은 개수에 따라 연산을 진행하는 재귀함수
    global max_sum, min_sum
    if idx == limit:    # 연산자를 다 사용하면 최대, 최소 체크
        if max_sum < initial:
            max_sum = initial
        if min_sum > initial:
            min_sum = initial

    else:
        for i in range(4):    # +, -, *, / 각각 시도해 보기
            if i == 0 and cal[i] != 0:    # +가 남아있으면 1개 감소시키고 배열의 다음 값을 더함
                cal[i] -= 1
                f(initial+num[idx+1], idx+1, limit)    # 다음 단계로 진행
                cal[i] += 1
            elif i == 1 and cal[i] != 0:    # -
                cal[i] -= 1
                f(initial-num[idx+1], idx+1, limit)
                cal[i] += 1
            elif i == 2 and cal[i] != 0:    # *
                cal[i] -= 1
                f(initial*num[idx+1], idx+1, limit)
                cal[i] += 1
            elif i == 3 and cal[i] != 0:    # / (음수를 나눌 때에는 //를 쓰면 소수점 버림이 아니라 올림이 될 수도 있으니 조심)
                cal[i] -= 1
                f(int(initial/num[idx+1]), idx+1, limit)
                cal[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal = list(map(int, input().split()))
    num = list(map(int, input().split()))

    max_sum = -100000000
    min_sum = 100000000
    f(num[0], 0, N-1)

    diff = max_sum - min_sum
    print(f"#{tc} {diff}")
