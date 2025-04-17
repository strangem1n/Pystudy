import math


def solve(M, N, x, y):
    i = 0
    if M < N:
        M, N, x, y = N, M, y, x
    while i * M + x < lcm:
        if (i * M + x) % N == y:
            return i * M + x
        i += 1
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    lcm = math.lcm(M, N)
    if M == x and N == y:
        print(lcm)
    else:
        if M == x:
            x = 0
        if N == y:
            y = 0
        result = solve(M, N, x, y)
        if result > lcm:
            print(-1)
        else:
            print(result)