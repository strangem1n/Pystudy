def f(cnt):
    if cnt == m:
        print(*result)

    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                result[cnt] = arr[i]
                f(cnt+1)
                result[cnt] = 0
                used[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [0] * n
result = [0] * m
f(0)
