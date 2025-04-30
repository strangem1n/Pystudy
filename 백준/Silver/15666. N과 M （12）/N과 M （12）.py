def f(cnt, prev):
    if cnt == m:
        if p not in result:
            result.append(p[:])

    else:
        for i in range(prev, n):
            p[cnt] = arr[i]
            f(cnt+1, i)
            p[cnt] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
p = [0] * m
result = []
f(0, 0)
for subset in result:
    print(*subset)
