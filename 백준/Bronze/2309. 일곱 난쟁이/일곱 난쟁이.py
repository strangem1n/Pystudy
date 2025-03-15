def f(n):
    if n == 7:
        result = sum(p)
        if result == 100:
            for i in range(7):
                ans[i] = p[i]

    else:
        for i in range(9):
            if used[i] == 0:
                used[i] = 1
                p[n] = dwarf[i]
                f(n+1)
                used[i] = 0


dwarf = [int(input()) for _ in range(9)]
used = [0] * 9
p = [0] * 7
ans = [0] * 7
f(0)
ans.sort()
for i in ans:
    print(i)
