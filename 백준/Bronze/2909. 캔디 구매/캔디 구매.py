c, k = map(int, input().split())
if k == 0:
    print(c)
else:
    money = 10 ** k
    chk_round = c % money
    if money // 2 > chk_round:
        print(c-chk_round)
    else:
        print(c-chk_round+money)
