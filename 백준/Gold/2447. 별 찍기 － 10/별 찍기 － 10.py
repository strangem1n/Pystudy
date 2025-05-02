def f(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        up = list(map(lambda x: x*3, f(n//3)))
        middle = list(map(lambda x: x+' '*(n//3)+x, f(n//3)))
        down = list(map(lambda x: x*3, f(n//3)))
        return up+middle+down

star = f(int(input()))
for s in star:
    print(s)
