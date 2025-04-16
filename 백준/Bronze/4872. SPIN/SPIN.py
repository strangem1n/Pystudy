start = list(map(int, input()))
l = len(start)
while True:
    try:
        spin = list(map(int, input()))
        for i in range(l):
            start[i] += spin[i]
    except EOFError:
        print(''.join(map(lambda x: str(x%10), start)))
        break
