def chk():
    for i in range(r):
        for j in range(c):
            if pic[i][j] == '#':
                return False
    return True


T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    pic = list(list(input()) for _ in range(r))

    for i in range(r):
        for j in range(c):
            if pic[i][j] == '#':
                if i+1 < r and j+1 < c and pic[i][j] == pic[i+1][j] == pic[i][j+1] and pic[i+1][j+1]:
                    pic[i][j] = '/'
                    pic[i][j+1] = '\\'
                    pic[i+1][j] = '\\'
                    pic[i+1][j+1] = '/'

    print(f'Case #{tc}:')
    if chk():
        for i in range(r):
            print(''.join(pic[i]))
    else:
        print('Impossible')
