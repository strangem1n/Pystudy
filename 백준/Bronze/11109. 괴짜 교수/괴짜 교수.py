T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    if d+p*n == s*n:
        print('does not matter')
    elif d+p*n > s*n:
        print('do not parallelize')
    else:
        print('parallelize')
