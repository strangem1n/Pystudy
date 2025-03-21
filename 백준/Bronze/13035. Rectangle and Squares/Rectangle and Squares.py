t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    phil = a * b
    elijah = c ** 2
    num = phil // elijah
    over = elijah * (num+1) - phil
    under = phil - elijah * num
    result = 0
    if over < under:
        result = elijah * (num+1)
    else:
        result = elijah * num

    if result == 0:
        result = elijah
    print(result)
