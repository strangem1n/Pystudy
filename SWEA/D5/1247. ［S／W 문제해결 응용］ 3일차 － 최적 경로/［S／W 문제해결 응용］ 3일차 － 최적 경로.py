def move(n):    # 순열로 만들어진 경로에 따른 이동 거리 구하기
    result = abs(office_x - arr[p[0]*2]) + abs(office_y - arr[p[0]*2+1])    # 회사에서 시작
    for i in range(n-1):
        result += abs(arr[p[i]*2] - arr[p[i+1]*2]) + abs(arr[p[i]*2+1] - arr[p[i+1]*2+1])
    result += abs(arr[p[n-1]*2] - home_x) + abs(arr[p[n-1]*2+1] - home_y)    # 집에서 끝
    return result


def f(n, limit):
    global min_distance
    if n == limit:
        ans = move(limit)
        if min_distance > ans:
            min_distance = ans
    else:
        for i in range(limit):    # 재귀로 고객 방문 순열 뽑아내기
            if used[i] == 0:
                used[i] = 1
                p[n] = i
                f(n+1, limit)
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    office_x, office_y, home_x, home_y, *arr = list(map(int, input().split()))
    used = [0] * N
    p = [0] * N
    min_distance = (100+100)*12    # 이동거리 초기값: 극단적인 값
    f(0, N)
    print(f"#{tc} {min_distance}")
