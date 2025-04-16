matches = {
    1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6
}


def chk(num):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    if (i * 10 + j) + (k * 10 + m) > 99:
                        continue
                    p = (i+k+(j+m)//10)
                    if p > 9:
                        continue
                    q = (j+m) % 10
                    if matches[i] + matches[j] + matches[k] + matches[m] + matches[p] + matches[q] == num:
                        return i, j, k, m, p, q
    return False


n = int(input())
n -= 4
if chk(n):
    a, b, c, d, e, f = chk(n)
    print(f'{a}{b}+{c}{d}={e}{f}')
else:
    print('impossible')
