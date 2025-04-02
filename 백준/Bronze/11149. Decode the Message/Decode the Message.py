T = int(input())
for _ in range(T):
    message = input().split()
    for m in message:
        decode = 0
        for i in range(len(m)):
            decode += ord(m[i])-97
        decode = (decode % 27)
        if decode == 26:
            print(' ', end='')
        else:
            print(chr(decode+97), end='')
    print('')
