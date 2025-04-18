def f(n):
    if n > 1022:
        return -1

    num = [0]
    cnt = 0
    while cnt < n:
        cnt += 1
        num[0] += 1
        while True:
            if num[-1] == 10:
                num[-1] = 0
                num.append(1)
            brk = False
            for i in range(len(num) - 1):
                if num[i] >= num[i + 1]:
                    num[i] = 0
                    num[i + 1] += 1
                    brk = True
                    break
            if brk:
                continue
            else:
                break
        if len(num) > 10:
            return -1
    return ''.join(map(lambda x: str(x), num[::-1]))


print(f(int(input())))
