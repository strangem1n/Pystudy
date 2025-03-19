def f(cnt, num, limit):
    if cnt == limit:
        print(*p)

    else:
        for i in range(1, num+1):
            if p[cnt-1] <= i:
                p[cnt] = i
                f(cnt+1, num, limit)
                p[cnt] = 0


n, m = map(int, input().split())
used = [0] * (n+1)
p = [0] * m
f(0, n, m)
