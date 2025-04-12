import sys, math
input = sys.stdin.readline


def f(x):
    sq = math.sqrt(x)
    if sq != int(sq):
        return False

    x = int(str(x)[::-1])
    sq = math.sqrt(x)
    if sq != int(sq):
        return False

    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if f(n):
        print('YES')
    else:
        print('NO')
