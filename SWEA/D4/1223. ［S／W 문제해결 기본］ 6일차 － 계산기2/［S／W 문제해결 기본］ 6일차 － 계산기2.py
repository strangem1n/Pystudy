for tc in range(1, 11):
    n = int(input())
    exp = list(map(lambda x: x.split('*'), input().split('+')))
    for i in range(len(exp)):
        if len(exp[i]) > 1:
            temp = 1
            for num in exp[i]:
                temp *= int(num)
            exp[i] = temp
        else:
            exp[i] = int(exp[i][0])
    print(f"#{tc} {sum(exp)}")
