def divide(num, previous, arr_a, arr_b, cnt):
    global answer

    if cnt == num // 2:    # A음식 구성완료
        for i in range(num):    # 아직 고르지 않은 식재료로 B음식 구성하기
            if used[i] == 0:
                arr_b.append(i)
        s_a = synergy(num, arr_a)    # 각 음식의 시너지값 구하기
        s_b = synergy(num, arr_b)
        if answer > abs(s_a - s_b):    # 최솟값 갱신하기
            answer = abs(s_a - s_b)
        while arr_b:
            arr_b.pop()    # B음식 구성 식재료 초기화

    else:
        for i in range(previous+1, num):    # 조합을 만들기 위해 이전에 선택했던 원소 다음부터 고르기
            if used[i] == 0:    # 아직 선택하지 않은 식재료로 A음식 구성
                used[i] = 1
                arr_a.append(i)
                divide(num, i, arr_a, arr_b, cnt+1)    # 재귀함수로 조합 만들기
                used[i] = 0
                arr_a.pop()


def synergy(num, array):
    result = 0
    for i in range(num//2):
        for j in range(num//2):    # 음식 구성하는 식재료 2개씩 골라 시너지값 더하기. 
            result += arr[array[i]][array[j]]    # S_12와 S_21을 모두 더하므로 원소 2개인 순열 만들어서 인덱스 접근
            # i==j인 경우 시너지값은 자연스럽게 0이라서 예외처리 필요 X.
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    answer = float("inf")
    divide(N, -1, [], [], 0)
    print(f"#{tc} {answer}")
