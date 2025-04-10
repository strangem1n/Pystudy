def find():
    for i in range(l-1, -1, -1):
        for j in range(i, -1, -1):
            if sq[i] + sq[j] > n:
                continue
            elif sq[i] + sq[j] == n:
                print(2)
                return True
    return False


def next_find():
    for i in range(l-1, -1, -1):
        for j in range(i, -1, -1):
            if sq[i] + sq[j] > n:
                continue
            for k in range(j, -1, -1):
                if sq[i] + sq[j] + sq[k] == n:
                    return True


n = int(input())
sq = [i**2 for i in range(1, int(n**(1/2))+1)]
l = len(sq)

if sq[-1] == n:
    print(1)
else:
    chk = find()
    if not chk:
        chk2 = next_find()
        if chk2:
            print(3)
        else:
            print(4)
