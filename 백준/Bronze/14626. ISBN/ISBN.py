import sys
input = sys.stdin.readline

isbn = input().rstrip()
chk = 0
even = False
for i in range(13):
    if i % 2 == 1:
        if ord(isbn[i]) != 42:
            chk += int(isbn[i]) * 3
        else:
            even = True
    else:
        if ord(isbn[i]) != 42:
            chk += int(isbn[i])

for i in range(10):
    if even and (i*3 + chk) % 10 == 0:
        print(i)
        break
    elif not even and (i + chk) % 10 == 0:
        print(i)
        break