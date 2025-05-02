n, m = map(int, input().split())
a, b = map(int, input().split())

for i in range(n*m):
    if i // m < a:
        print('S', end='')

    elif i // m > a:
        print('N', end='')

    else:
        if i % m > b:
            print('W', end='')
        else:
            print('E', end='')

    if i % m == m - 1:
        print('')
