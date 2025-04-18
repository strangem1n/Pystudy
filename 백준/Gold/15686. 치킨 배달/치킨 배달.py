def find():
    house_locate = []
    chicken_locate = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house_locate.append([i, j])
            elif city[i][j] == 2:
                chicken_locate.append([i, j])
    return house_locate, chicken_locate


def chicken_length(r, c):
    min_length = float('inf')
    for i in range(len(chicken)):
        if p[i] == 0:
            cr, cc = chicken[i]
            length = abs(cr-r) + abs(cc-c)
            min_length = min(length, min_length)
    return min_length


def delete_chickens(cnt, prev):
    global total_min_length
    if cnt == 0:
        min_length = 0
        for hr, hc in house:
            min_length += chicken_length(hr, hc)
            if min_length >= total_min_length:
                return
        total_min_length = min(total_min_length, min_length)

    else:
        for i in range(prev+1, len(chicken)):
            if p[i] == 0:
                p[i] = 1
                delete_chickens(cnt-1, i)
                p[i] = 0


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house, chicken = find()
p = [0] * len(chicken)
have_to_delete = len(chicken) - m
total_min_length = float('inf')
delete_chickens(have_to_delete, -1)
print(total_min_length)
