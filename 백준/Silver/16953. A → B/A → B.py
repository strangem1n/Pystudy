a, b = map(int, input().split())

cnt = 1
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break
    cnt += 1
if b == a:
    print(cnt)
else:
    print(-1)
