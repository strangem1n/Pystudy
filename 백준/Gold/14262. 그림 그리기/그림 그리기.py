import sys
input = sys.stdin.readline

def cnt():
    r = g = b = 0
    for i in range(len(canvas)):
        for j in range(len(canvas[0])):
            if canvas[i][j] == 'R':
                r += 1
            elif canvas[i][j] == 'G':
                g += 1
            elif canvas[i][j] == 'B':
                b += 1
    return r, g, b

def overwrite(start):
    dr = dg = db = 0
    for i in range(start, n+start):
        for j in range(start, m+start):
            if draw[i-start][j-start] != '.':
                if canvas[i][j] == 'R':
                    dr -= 1
                elif canvas[i][j] == 'G':
                    dg -= 1
                elif canvas[i][j] == 'B':
                    db -= 1
                canvas[i][j] = draw[i-start][j-start]
                if canvas[i][j] == 'R':
                    dr += 1
                elif canvas[i][j] == 'G':
                    dg += 1
                elif canvas[i][j] == 'B':
                    db += 1
    return dr, dg, db

n, m, t = map(int, input().split())
draw = [list(input().rstrip()) for _ in range(n)]
min_add = min(m, n)
canvas = [[None] * (m+min_add) for _ in range(n+min_add)]

if t <= min_add:
    for k in range(t):
        overwrite(k)
    init_r, init_g, init_b = cnt()
    print(init_r)
    print(init_g)
    print(init_b)
else:
    for k in range(min_add-1):
        overwrite(k)
    init_r, init_g, init_b = cnt()
    diff_r, diff_g, diff_b = overwrite(min_add-1)
    print(init_r + diff_r*(t-min_add+1))
    print(init_g + diff_g*(t-min_add+1))
    print(init_b + diff_b*(t-min_add+1))