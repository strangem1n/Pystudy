def dfs(queen, limit):
    global result
    if queen == limit:
        result += 1

    else:
        for i in range(limit):
            if used_column[i] == 0 and cross_plus[i+queen] == 0 and cross_minus[limit-1+i-queen] == 0:
                used_column[i] = 1
                cross_plus[queen+i] = 1
                cross_minus[limit-1+i-queen] = 1
                dfs(queen+1, limit)
                used_column[i] = 0
                cross_plus[queen+i] = 0
                cross_minus[limit-1+i-queen] = 0


n = int(input())
used_column = [0] * n
cross_plus = [0] * (2 * (n-1) + 1)
cross_minus = [0] * (2 * (n-1) + 1)
result = 0
dfs(0, n)
print(result)
