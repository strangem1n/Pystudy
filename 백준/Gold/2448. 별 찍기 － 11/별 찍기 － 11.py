def f(cnt):
    if cnt == 3:
        star = ['  *  ', ' * * ', '*****']
        return star

    else:
        up = list(map(lambda x: ' '*(cnt//2)+x+' '*(cnt//2), f(cnt//2)))
        down = list(map(lambda x: x+' '+x, f(cnt//2)))
        return up+down


result = f(int(input()))
for stars in result:
    print(stars)
