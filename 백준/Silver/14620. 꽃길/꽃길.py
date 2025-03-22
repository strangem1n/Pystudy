def flower(n, cnt, cost):
    global min_cost
    if cost > min_cost:
        return

    if cnt == 3:
        if min_cost > cost:
            min_cost = cost

    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if possible[i][j] and possible[i+1][j] and possible[i][j+1] and possible[i-1][j] and possible[i][j-1]:
                    possible[i][j] = possible[i+1][j] = possible[i][j+1] = possible[i-1][j] = possible[i][j-1] = 0
                    flower_cost = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i-1][j] + arr[i][j-1]
                    flower(n, cnt+1, cost+flower_cost)
                    possible[i][j] = possible[i+1][j] = possible[i][j+1] = possible[i-1][j] = possible[i][j-1] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

possible = [[1] * N for _ in range(N)]
min_cost = 200*5*3
flower(N, 0, 0)
print(min_cost)