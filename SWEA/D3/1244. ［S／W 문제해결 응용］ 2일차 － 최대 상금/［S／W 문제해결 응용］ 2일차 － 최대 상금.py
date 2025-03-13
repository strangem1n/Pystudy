def f(n, cnt, typ):
    global max_result
    if cnt == 0:  # 교환이 끝나면
        result = int("".join(num))  # 숫자판의 숫자를 합쳐서 정수로 변환
        if max_result < result:
            max_result = result

    elif num == ideal:    # 아직 교환 횟수가 남았는데 이상적인 상태(최대 금액) 되어버리면
        # 교환횟수가 짝수 번 남았으면, 임의의 두 자리를 선택해서 그것들끼리 계속 바꾸면 원래 상태로 되돌아가기 때문에 상관없다.
        # 예시: AB -> BA -> AB
        if cnt % 2 == 1:    # 홀수 번 교환이 남았으면 (2k+1) 번 교환해야 하므로 최소 1번은 원하지 않게 교환할 가능성이 있다.
            same_num = False
            for i in range(n):
                for j in range(n):
                    if i != j:
                        if ideal[i] == ideal[j]:    # 숫자판에 같은 숫자가 있는지 확인
                            same_num = True
                            break
                if same_num:    # 같은 숫자가 있으면, 같은 숫자끼리 바꿔서 그대로 유지할 수 있다.
                    break
            if not same_num:    # 같은 숫자가 없으면, 마지막 두 자리를 한 번은 바꿔야 조건을 만족하게 된다.
                ideal[-1], ideal[-2] = ideal[-2], ideal[-1]
        max_result = int("".join(ideal))
        return

    elif typ == "brute":
        for i in range(n):
            for j in range(n):
                if i != j:
                    if num[i] == num[j]:
                        f(n, cnt - 1, typ)
                    else:
                        num[i], num[j] = num[j], num[i]  # 숫자판에서 서로 다른 2개를 교환
                        f(n, cnt - 1, typ)  # 남은 교환 횟수 1회 감소
                        num[i], num[j] = num[j], num[i]  # 재귀가 끝나면 원래대로 되돌려줌

    elif typ == "greedy":    # 교환 횟수가 자릿수와 같거나 더 많아지면, 굳이 브루트포스로 접근할 필요 없다.
        i = 0
        while num[i] == ideal[i]:    # 현재 숫자판과 이상적인 상태를 비교해 다른 자릿수를 찾기
            i += 1
        for j in range(i + 1, n):    # 현재 자리에 와야 하는 이상적인 숫자는 어디에 있는지 찾기
            if num[j] == ideal[i]:    # 찾으면 둘이 바꾸고 교환횟수 1 감소
                num[i], num[j] = num[j], num[i]
                break
        f(n, cnt - 1, typ)    # 이상적인 상태가 될 때까지 반복


T = int(input())
for tc in range(1, T + 1):
    num, swap = input().split()
    num, swap = list(num), int(swap)  # 숫자판은 리스트로, 바꿔야 하는 횟수는 정수로
    ideal = sorted(num, reverse=True)    # 이상적인 숫자판
    max_result = 0  # 가장 큰 금액
    if swap < len(num):
        keyword = "brute"
    else:
        keyword = "greedy"
    f(len(num), swap, keyword)
    print(f"#{tc} {max_result}")
