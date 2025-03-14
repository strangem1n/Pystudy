T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    min_tower = 10000 * N

    for i in range(1<<N):    # 비트 연산으로 점원의 부분집합 구하기
        result = 0
        for j in range(N):
            if i & (1<<j):
                result += arr[j]    # 부분집합의 점원 키 더해주기

        if result == B:    # 목표 높이와 동일하면 바로 종료
            min_tower = result
            break
        elif result > B and (min_tower - B) > (result - B):    # 목표 높이로 만들지 못하면 최대한 차이가 적게 만들기
            min_tower = result

    print(f"#{tc} {min_tower - B}")
