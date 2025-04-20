def f(cnt, prev):
    if cnt == 6:
        print(*lotto)

    else:
        for i in range(prev+1, k):
            if used[i] == 0:
                used[i] = 1
                lotto[cnt] = s[i]
                f(cnt+1, i)
                used[i] = 0

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break

    used = [0] * k
    lotto = [0] * 6
    f(0, -1)
    print('')
