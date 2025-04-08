import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
        return rep[x]
    else:
        return x


def union(x, y):
    rep[find_set(x)] = find_set(y)


n, m = map(int, input().split())
rep = [i for i in range(n+1)]
for _ in range(m):
    chk, a, b = map(int, input().split())
    if chk == 0:
        if a == b:
            continue
        union(a, b)
    else:
        if a == b:
            print('YES')
        elif find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
