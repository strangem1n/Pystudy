def f(i, j):
    global cnt
    if i == j == n-1:
        cnt += 1

    else:
        if house[i][j] in [2, 3]:
            if j+1 < n and house[i][j+1] == 0:
                house[i][j+1] = 2
                f(i, j+1)
                house[i][j+1] = 0
        if house[i][j] in [2, 3, 4] and i+1 < n and j+1 < n and house[i][j+1] == house[i+1][j] == house[i+1][j+1] == 0:
            house[i+1][j+1] = 3
            f(i+1, j+1)
            house[i+1][j+1] = 0
        if house[i][j] in [3, 4]:
            if i+1 < n and house[i+1][j] == 0:
                house[i+1][j] = 4
                f(i+1, j)
                house[i+1][j] = 0

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

house[0][1] = 2
cnt = 0
f(0, 1)
print(cnt)